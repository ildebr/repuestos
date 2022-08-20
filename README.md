# repuestos

## Installation 

```
pip install -r requirements.txt
```

## Usage

The endpoints
```
repuestos/<int:pk>/
repuestos/
venta/<int:pk>/
venta/
reporte/<int:pk>/
reporte/
```

The two repuestos endpoints return info about a particular repuesto or a list of every repuesto.
The venta/<int:pk> returns data about an specific sale while venta/ returns every sale, in addition venta/ can be passed a queryparameter 'page=number' to paginate the results, it will return 5 entries per page.
The reporte endpoint works receiving two date values that represent an early date and late date, then it will make a report containing every sale made between these dates.
Every main endpoint (those without an extra route parameter) can be used to return either a list of data or to send the data to populate the database.
