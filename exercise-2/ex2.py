import requests, pathlib, re

# check for ip.log file
file = pathlib.Path("ip.log")
if not file.exists ():
  print ("log file does not exist, fetching...")
  # if file is not present, perform a get request
  try:
    r = requests.get("https://raw.githubusercontent.com/linuxacademy/content-elastic-log-samples/master/access.log")
  except requests.exceptions.RequestException as e:
    raise SystemExit(e)
  # push request data into file
  try:
    with open('ip.log', 'wb') as f:
      f.write(r.content)
  except IOError as e:
    raise SystemExit(e)
else:
  print ("log file already exists")

# dict to store & lookup unique ips
ips = {}

# process file line by line extracting IPs (using regex)
# push unique IPs into a results.txt
try:
  f = open('ip.log')
  w = open('result.txt', 'w')
  for line in f:
    ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).group()
    if ip not in ips:
      ips[ip] = ''
      w.write(ip+'\n')
except IOError as e:
  raise SystemExit(e)
finally:
  f.close()
  w.close()

print(str(len(ips)) + ' unique IPs extracted. Open result.txt to view the list.')
print('Done.')
