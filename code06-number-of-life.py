from jdatetime import datetime
birthday = input('pleas enter your birthday: (yy-mm-dd)')
birthday = datetime.strptime(birthday, '%y-%m-%d')
today = datetime.now()
(today - birthday).days