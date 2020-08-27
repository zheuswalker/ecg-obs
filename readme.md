# Installation
`virtualenv flask` <br>
`cd flask`<br>
`source bin/activate`<br>
`pip install flask`<br>
`pip install requests`<br>

# run script
`python analyze.py`<br>

# if it says already running
`sudo kill $(sudo lsof -t -i:5000)`<br>

# if run but 404 check ufw
`ufw enable`<br>

# check port 5000 if open
`ufw status numbered`<br>

# enable port 5000 if closed
`ufw enable 5000/tcp`<br>
`ufw enable 5000/udp`<br>

# DONT LEAVE YOUR SESSION NOT OPENING PORT 22 FOR SSH
`ufw enable 22/tcp`<br>
`ufw enable 22/udp`<br>

# sample query
`curl --location --request POST 'http://206.189.87.169:5000/analyze_ecg' \
--form 'period=4' \
--form 'factor=0.1234' \
--form 'data=-127 -126 -125 -124 -123  '`


# Change Host and Port in Analyze.py
`analyze.py line 49`<br>

# run script in background
`nohup python analyze.py`<br>
