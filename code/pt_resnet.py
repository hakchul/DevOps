import argparse
from pathlib import Path
# import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim

import torchvision
import torchvision.transforms as transforms


LR = 0.001
BATCH = 64
EPOCHS = 100
NUM_CLASSES = 10
PATH_DATA = 'tmp/dataset'
PATH_CKPT = 'tmp/checkpoint'


@torch.no_grad()
def validate_network(dataloader, model):
    model.eval()

    num_correct = 0
    num_predict = 0
    accuracy = 0
    print('Running validation...')
    for step, (t_samples, t_labels) in enumerate(dataloader):
        if torch.cuda.is_available():
            t_samples = t_samples.cuda()
            t_labels = t_labels.cuda()
        outputs = model(t_samples)
        pred = torch.argmax(outputs, 1)
        num_correct += torch.sum(pred == t_labels).item()
        num_predict += len(t_labels)
    accuracy = num_correct / num_predict * 100
    print(f'Validation correct/predict: {num_correct}/{num_predict}')

    return accuracy



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--path_data', help='path of dataset', type=str, default=PATH_DATA)
    parser.add_argument('--path_ckpt', help='path of checkpoint', type=str, default=PATH_CKPT)
    parser.add_argument('--batch', help='batch size', type=int, default=BATCH)
    parser.add_argument('--epochs', help='number of epochs', type=int, default=EPOCHS)
    parser.add_argument('--lr', help='learning rate', type=float, default=LR)
    parser.add_argument('--val_freq', default=10, type=int, help="Epoch frequency for validation.")
    args = parser.parse_args()

    path_dataset = Path(args.path_data)
    path_output = Path(args.path_ckpt)
    path_output.mkdir(parents=True, exist_ok=True)

    # load dataset
    trans_train = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])
    trans_valid = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])
    ds_train = torchvision.datasets.STL10(path_dataset, split='train', download=True, transform=trans_train)
    ds_valid = torchvision.datasets.STL10(path_dataset, split='test', download=True, transform=trans_valid)
    dl_train = torch.utils.data.DataLoader(ds_train, batch_size=BATCH, shuffle=True)
    dl_valid = torch.utils.data.DataLoader(ds_valid, batch_size=BATCH, shuffle=True)
    # dl_train = torch.utils.data.DataLoader(ds_train, batch_size=BATCH, shuffle=True, num_workers=10)   # setting num_workers cause very low performance in windows 
    # dl_valid = torch.utils.data.DataLoader(ds_valid, batch_size=BATCH, shuffle=True, num_workers=10)

    model = torchvision.models.resnet18(num_classes=NUM_CLASSES)
    if torch.cuda.is_available():
        model.cuda()
        if torch.cuda.device_count() > 1:
            model = nn.DataParallel(model)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=args.lr)
    milestones = [int(args.epochs*0.5), int(args.epochs*0.75)]
    scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones=milestones, gamma=0.1)

    best_acc = 0
    best_epoch = 0
    for epoch in range(args.epochs):
        running_loss=0
        model.train()
        for i, data in enumerate(dl_train, 0):
            t_inputs, t_labels = data
            if torch.cuda.is_available():
                t_inputs = t_inputs.cuda()
                t_labels = t_labels.cuda()
            # zero the parameter gradients
            optimizer.zero_grad()
            # forward + backward + optimize
            t_outputs = model(t_inputs)
            loss = criterion(t_outputs, t_labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
        print(f'[{epoch+1:3}/{args.epochs}] loss: {running_loss/len(dl_train):.4f}, lr: {optimizer.param_groups[0]["lr"]:.5f}')

        if (epoch+1) % args.val_freq == 0 or epoch == args.epochs-1:
            acc = validate_network(dl_valid, model)
            print(f"Accuracy at epoch {epoch+1} of the network on the {len(ds_valid)} validation data: {acc:.2f}%")
            if best_acc <= acc:
                best_epoch = epoch+1
                best_acc = acc
                path_ckpt = path_output / f"best_checkpoint.pth"
                torch.save(model.state_dict(), path_ckpt)
            print(f'Best accuracy: {best_acc:.2f}% @ epoch {best_epoch}')
            path_ckpt = path_output / f"checkpoint{epoch+1:04d}.pth"
            torch.save(model.state_dict(), path_ckpt)

        scheduler.step()


if __name__ == '__main__':
    main()

