# Intro to Databases and SQL
### Using DB2 on IBM Cloud

DDL - data definition language defines, drops, changes data  
DML - data manipulation language reads and modifies data  

```sql

-- DDL Examples
create table TABLENAME (
    COLUMN1 datatype,
    COLUMN2 datatype,
    COLUMN3 datatype,
        ...
    ) ;

drop table COUNTRY;
create table COUNTRY (
    ID integer PRIMARY KEY NOT NULL,
    CCODE char(2),
    NAME varchar(60)
    );

```

  
`SELECT` is a DML query and its output is a ResultSet  

`INSERT` is a DML used to modify data 
```sql
INSERT INTO TBL (COLS)
VALUES (DATA, DATA, DATA, ...)l
```

`UPDATE` and `DELETE` are DML queries for modifying data
Remember to carefully use it with `WHERE` clause  
```sql
update TABLE set col='newval' where col='criterion';

delete from TABLE where col='criterion';
```

