# IPTODataAPI

<br>

## About the IPTODataAPI Python Wrapper

The IPTODataAPI python wrapper is an independently developed project with the aim to 
provide an easy to use wrapper which enables data retrieval related to GR electricity 
demand, generation & markets, as published by the Greek Independent Power Transmission 
Operator (IPTO).


The IPTODataAPI provides the ability to download data directly from the API and 
have it parsed into a user-friendly pandas dataframe. All queries require a <i>file_type</i> argument, 
and can be extended by the <i>start_date</i> and <i>end_date</i> arguments in order to collect data for a certain time period.
All argument information can be found <a href="https://www.admie.gr/en/market/market-statistics/file-download-api">here</a>. 


The module can be installed with:

```bash
pip install IPTODataAPI
```

<br>

## Using the IPTODataAPI Python Wrapper

IPTO allows you to query data as daily files that can be downloaded as excel files via the links provided through the API.
The wrapper includes an API class which retrieves the file URLs to be downloaded. In order to use this functionality 
we should have additional functions that process each dataset according to its requirements.

### Querying Load Forecast Data

Here is an example of a function that inherits the API functionality and extends it to collect historical Day Ahead Load 
Forecast data over the whole system and across the individual zones:

```python
start_date = '2020-10-01'
end_date = '2020-10-02'

da_load_fcst = DayAheadLoadForecast(start_date=start_date, end_date=end_date).main()

da_load_fcst.head()
```

<table border="1" class="dataframe"> <thead>  <tr style="text-align: right;"> <th>(MW)</th>      <th>System Total</th>      <th>Market Total</th>      <th>Market SOUTH-Zone</th>      <th>Market NORTH-Zone</th>      <th>Version</th>    </tr>    <tr>      <th>Date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2020-10-01 00:00:00</th>      <td>4290</td>      <td>4182</td>      <td>2593</td>      <td>1589</td>      <td>1</td>    </tr>    <tr>      <th>2020-10-01 00:00:00</th>      <td>4270</td>      <td>4163</td>      <td>2581</td>      <td>1582</td>      <td>2</td>    </tr>    <tr>      <th>2020-10-01 01:00:00</th>      <td>4020</td>      <td>3919</td>      <td>2430</td>      <td>1489</td>      <td>1</td>    </tr>    <tr>      <th>2020-10-01 01:00:00</th>      <td>4000</td>      <td>3900</td>      <td>2418</td>      <td>1482</td>      <td>2</td>    </tr>    <tr>      <th>2020-10-01 02:00:00</th>      <td>3870</td>      <td>3773</td> <td>2339</td> <td>1434</td> <td>1</td> </tr> </tbody></table>

<br>

```

Please let me know if you have any questions or issues with accessing any of the market data via the IPTO API.

E-mail: stratis.andreas@hotmail.com