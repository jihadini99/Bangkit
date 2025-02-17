def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type =="login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines


file_contents = file_contents.split()
    for i in file_contents: #i as word
        c = "" #as a character
        for letter in i:
            if c not in punctuations:
                c += letter
        if c not in uninteresting_words:
            if c not in dict.keys():
                interest[c]=1
            else:
                dict[character]+=1
            

def generate_report(machines):
    for machine, users in machines.items():
        if len(users)>0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user
    