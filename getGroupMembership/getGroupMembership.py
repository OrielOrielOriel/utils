#!/usr/bin/python3
import json
import sys

HELP = '''
Parses Bloodhound files: groups.json and users.json
and creates a file of each user's group membership in
the following format: user \\t group1,group2,group3

Syntax:

./getGroupMembership.py groups.json users.json output.txt
'''

if len(sys.argv) != 4:
	print(HELP)
	exit(1)

def removeAtSign(username: str) -> str:
	ret = ""

	for character in username:
		if character == "@":
			break
		else:
			ret += character

	return ret

gFile = sys.argv[1] 
uFile = sys.argv[2]
oFile = sys.argv[3]

with open(oFile, 'w') as outputFile, open(uFile, 'r') as usersFile, open(gFile, 'r') as groupsFile:
	# usersJsonObj.keys() == dict_keys(['users', 'meta'])
	# usersJsonObj['users'][0].keys() == dict_keys(['AllowedToDelegate', 'PrimaryGroupSid', 'HasSIDHistory', 'ObjectIdentifier', 'Aces', 'SPNTargets', 'Properties'])
	# usersJsonObj['users'][0]['Properties'].keys() == dict_keys(['distinguishedname', 'domain', 'name', 'objectid', 'unconstraineddelegation', 'passwordnotreqd', 'highvalue'])
	usersJsonObj = json.load(usersFile)

	# groupJsonObj.keys() = dict_keys(['groups', 'meta'])
	groupsJsonObj = json.load(groupsFile)

	# Gets written to file later
	bigUserDict = {}

	print("This is gonna take a while...") # This shouldn't be in Python lol

	# groupDict.keys() == dict_keys(['Aces', 'ObjectIdentifier', 'Properties', 'Members'])
	for groupDict in groupsJsonObj['groups']:

		# userDict.keys() == dict_keys(['MemberType', 'MemberId'])
		for userDict in groupDict['Members']:

			# groupDict['Properties'].keys() == dict_keys(['distinguishedname', 'domain', 'highvalue', 'objectid', 'name'])
			memberId = userDict['MemberId']
			groupName = removeAtSign(groupDict['Properties']['name'])
			userName = ""

			for userObj in usersJsonObj['users']:
				if not userObj['ObjectIdentifier'] == memberId:
					pass
				else: 
					userName = userObj['Properties']['name']
					break

			if userName in bigUserDict:
				bigUserDict[userName].append(groupName)
			else:
				bigUserDict.update({userName: [groupName]})
	
	for user in bigUserDict.keys():
		groupString = ','.join(bigUserDict[user])
		line = f"{user}\t{groupString}\n"

		outputFile.write(line)
