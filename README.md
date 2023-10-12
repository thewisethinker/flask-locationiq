# flask-locationiq
LocationIQ geocoding api with Flask

Install Flask, Waitress and ready to go

http://url/geo?q=<querystring=PIN or anything>

boundingbox element of the returned result will give the coverage area of the queried string.

For a PIN for an example, result may return an array of entries with different locations. In such a case, you may match the coutry name, state name, district name or locality etc. to get the intended queried area.


