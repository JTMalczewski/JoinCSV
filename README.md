# JoinCSV
## recruitment task
> Implement an executable program, which will read two csv files, join them using a specified column and then write the result to the standard output. Users should be able to specify the join type (inner, left or right).

### Technologies
Project is created with:
- NumPy 1.17.4
- Python 3.8.10

### General information
This project heavily operates on NumPy functionality, mainly because of the clarity of code and its performance. Despite that comparing two columns is the most overloading moment that could be optimized.<br /><br />
All code was created in three workdays during breaks from university classes.

### Launch
To start the merging script run: <br /> 
```bash
$ python3 join.py file_path file_path column_name join_type`
```
`file_path` - linuks path to csv datafile conform to the [rfc4180](https://datatracker.ietf.org/doc/html/rfc4180)<br />
`column_name` - choose the header of your column from data file for join operation<br />
`join_type` - choose `inner`, `left` or `right`.<br />
<br /> By default join type is set to `inner`. This solution helps to spot significant lines and don't generate empty cells. To read more about join types, I recommend [metabase.com](https://www.metabase.com/learn/sql-questions/sql-join-types) article (basic SQL knowledge is needed).<br /><br />

This repository includes two CSV data files for testing. You can try using them by this command in the root folder:
```bash
$ python3 join.py tools/databases/hw_200.csv tools/databases/hw_25000.csv " Height" left
```

### Attached databases
Test CSV files [source](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html):
- hw_200.csv `3.7 kB`
- hw_25000.csv `633,3 kB`

