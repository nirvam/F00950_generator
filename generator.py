import sys
import os

cur_dir=sys.path[0]
print(cur_dir)

sql="insert into ps810.sy810.f00950 values ('3','{}','{}','{}','{}','{}','                                        ','          ','    ','Y','{}',' ',' ',' ',' ','                              ','0',' ',' ',' ',' ',' ',' ',' ','PSFT      ','EP00950   ','CN4SJDEPY0','115209','145618','0','0','0',' ');"
sql_all="insert into ps810.sy810.f00950 values ('3','{}','*ALL      ','          ','                              ','    ','                                        ','          ','    ','N','N','Y','Y','Y','Y','                              ','0','C',' ',' ',' ',' ',' ',' ','PSFT      ','EP00950   ','CN4SJDEPY0','115211','161346','0','0','0','                                                                                                                        ');"
roles='FSSRTRADM,FSSRTRFAAD,FSSRTRBKAD,FSSRTRTCAD,FSSRTRTL,FSSPTPADM,FSSPTPSNAD,FSSPTPPMAD,FSSPTPPMTL,FSSPTPFIAD,FSSPTPTL,FSSOTCBKAD,FSSOTCBLAD,FSSOTCCDAD,FSSOTCCRAD,FSSOTCPRAD,FSSOTCTL'.split(',')
table={}
for role in roles:
	table[role]=[]

obj_list={}
with open(os.path.join(cur_dir,'obj_list')) as f:
	for x in f.readlines():
		obj,sy=x.split()
		obj_list[obj]=sy
	
with open(os.path.join(cur_dir,'sec_metrix.csv')) as f:
	for i in f.readlines():
		Prog,Form,Version,*Marks=i.split(',')
		for j,mark in enumerate(Marks):
			if mark in ['A','W','R','C']:
				table[roles[j]].append(','.join([Prog,Form,Version]))

for key in table.keys():
	table[key]=set(table[key])

with open(r'/tmp/test_output.sql','w') as f:
	for role in table.keys():
		print(sql_all.format(role),file=f)
		for i in table[role]:
			Prog,Form,Version=i.split(',')
			try:
				print(sql.format(role,Prog,Form,Version,obj_list[Prog],'Y'),file=f)
			except:
				print(role,Prog,Form,Version)
