# DB

## Cassandra

### CQLSH

* Connection

    ```bash
    # cqlsh [ip] [options]
    cqlsh
    cqlsh 192.168.100.100
    cqlsh 192.168.100.100 --cqlversion 3.4.4
    ```

* COPY

    ```sql
    -- COPY table_name [ ( column_list ) ]
    --     TO 'file_name' [ , 'file2_name', ... ] | STDOUT
    --     [ WITH option = 'value' [ AND ... ] ]      
    COPY channels (id, title)
        TO 'channels.csv'
        WITH HEADER = TRUE;
    ```

    ```sql
    -- COPY table_name [ ( column_list ) ]
    --     FROM 'file_name'[ , 'file2_name', ... ] | STDIN
    --     [ WITH option = 'value' [ AND ... ] ]  
    COPY channels (id, title)
        FROM 'channels.csv'
        WITH HEADER = TRUE;
    ```

    > Number of column shoud be same

### Nodetool

* Info

    * Status

    ```bash
    # cluster information
    nodetool status
    nodetool status {KEY_SPACE}
    ```
    
    * Statistics
    ```bash
    # statistics on tables
    nodetool tablestats
    nodetool tablestats {KEY_SPACE}.{TABLE}

    # GC Statistics
    nodetool gcstats

    # network information
    nodetool netstats
    ```

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

        > Make sure the table schema exists. If necessary, truncate the table.

        ```bash
        # Locate the most recent snapshot folder:
        #   data_directory/keyspace/table_name-UUID/snapshots/snapshot_name
        # Copy the most recent snapshot SSTable directory to the data directory:
        #   data_directory/keyspace/table_name-UUID
        # Troubleshootings:
        #   Check file permissions

        # run refresh command for each table
        nodetool refresh keyspace table
        ```
