#Installation#
`virtualenv flask`
`cd flask`
`source bin/activate`
`pip install flask`
`pip install requests`

#run script
`python analyze.py`

#if it says already running
`sudo kill $(sudo lsof -t -i:5000)`

#if run but 404 check ufw
`ufw enable`

#check port 5000 if open
`ufw status numbered`

#enable port 5000 if closed
`ufw enable 5000/tcp`
`ufw enable 5000/udp`


#sample query
`curl --location --request POST 'http://206.189.87.169:5000/analyze_ecg' \
--form 'period=4' \
--form 'factor=0.1234' \
--form 'data=-127 -126 -125 -124 -123  '`


#Change Host and Port in Analyze.py
`analyze.py line 49`

#Run script in background
`nohup python analyze.py`
