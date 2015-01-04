import tweepy, sys, time
from keys import keys
import json
import os,random
import sys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth) 

user = sys.argv[1]
since_id_user = 0
#Get user timeline since the last read tweet
with open("since_id.txt") as f:
	user_sinceids = f.read()

#Get latest read tweet id
for user_sinceid in iter(user_sinceids.splitlines()):
	if user_sinceid.find(user)!= -1:
		since_id_user = user_sinceid.split('=')[-1]
		break

if since_id_user == 0:
	statuses = api.user_timeline(count = int(sys.argv[2]), screen_name=user)
else:
	statuses = api.user_timeline(screen_name=user,since_id=since_id_user)

#Exit if no new tweets are there
if not statuses:
	print "No new tweet"
	exit()

for status in reversed(statuses):
	#Tweet has image
	if status._json['entities'].has_key('media'):
		text = status._json['text']
		media_url_replace = status._json['entities']['media'][0]['url']
		#remove existing media from text
		text = '@'+user+' '+text.replace(media_url_replace,'')
		if len(text) > 140:
			text = text[0:120]
		#Get random image
		filename = 'images/'+random.choice(os.listdir("images"))
		try: 
			api.update_with_media(filename,status = text)
			print 'Status updated'
		except:
			print 'Some error'
			pass
	print '--------------'

#Get the id of the latest tweet
new_since_id=statuses[0].id

#If the user is read for the first time, append to the file content
#else modify the existing content
if since_id_user == 0:
	user_sinceids += '\n'+user+'='+str(new_since_id)
	new_user_sinceids = user_sinceids
else:
	new_user_sinceids = ''
	for user_sinceid in iter(user_sinceids.splitlines()):
		if user_sinceid.find(user) != -1:
			new_user_sinceid = user+'='+str(new_since_id)+'\n'
		else:
			new_user_sinceid = user_sinceid+'\n'
		new_user_sinceids += new_user_sinceid

with open("since_id.txt","w") as f:
	f.write(new_user_sinceids)

print "Ids updated"
print new_user_sinceids
