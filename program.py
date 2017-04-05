def main ():
    print_header()
    run_event_loop()


def print_header ():
    print('APP Giornaliera')


def run_event_loop():
    print('Benvenuto')
    cmd = None
    journal_data = []
    while cmd != 'x':

       cmd =input('1 per visualizzare il diario o 2 per aggiornare ed x per uscire')
       if cmd == '1':
           list_entries(journal_data)
       elif cmd == '2':
           add_entry(journal_data)

    print('Alla prossima')

def list_entries(data):
    print("Ecco cosa hai fatto oggi")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx+1, entry))

def add_entry(data):
    text = input("scrivi ciò che hai fatto oggi")
    data.append(text)

main()