import requests
import json

reg='https://cit-home1.herokuapp.com/api/rs_homework_1'
txt = json.dumps({'user': 32,'1':{"movie 10":2.329,"movie 23":3.306,"movie 30":3.122},'2':{"movie 32":4.03}})
head={'content-type': 'application/json'}

p = requests.post(reg, data=txt, headers=head)
print(p)
print(p.json())