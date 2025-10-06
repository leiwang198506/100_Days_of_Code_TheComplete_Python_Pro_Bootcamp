#List

US_states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
"Connecticut", "Massachusetts", "Maryland", "South Carolina",
"New Hampshire", "Virginia", "New York", "North Carolina",
"Rhode Island", "Vermont", "Kentucky", "Tennessee",
"Ohio", "Louisiana", "Indiana", "Mississippi",
"Illinois", "Alabama", "Maine", "Missouri",
"Arkansas", "Michigan", "Florida", "Texas", "Iowa",
"Wisconsin", "California", "Minnesota", "Oregon",
"Kansas", "West Virginia", "Nevada", "Nebraska",
"Colorado", "North Dakota", "South Dakota", "Montana",
"Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
"New Mexico", "Arizona", "Alaska", "Hawaii"]
print(US_states[49])
print(US_states[-1])
#change list item easily
US_states [1]="Pennsylvania"
print(US_states[1])
#add new item to the end of the list
US_states.append("LeiVille")
print(US_states[50])
US_states.extend(["haha","hehe","huhu"])
print(US_states)