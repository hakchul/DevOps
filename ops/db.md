# DB

## Cassandra

### CQLSH

* connect

    ```bash
    # cqlsh [ip] [options]
    cqlsh
    cqlsh 192.168.100.100
    cqlsh 192.168.100.100 --cqlversion 3.4.4
    ```

### Nodetool

* Backup and restore

    > <https://docs.datastax.com/en/cassandra/3.0/cassandra/operations/opsBackupRestore.html>

* Taking a snapshot

    ```bash
    # cleanup
    nodetool cleanup keyspace
    # take snapshots
    nodetool snapshot keyspace
    ```

* Deleting snapshot files

    ```bash
    nodetool clearsnapshot  # clear all
    nodetool clearsnapshot keyspace
    ```

* Restoring from a snapshot

    ```bash
    # run refresh command for each table
    nodetool refresh keyspace table
    ```
