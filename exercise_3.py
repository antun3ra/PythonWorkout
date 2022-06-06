def run_timing():
    total_list = []
    time = 0

    while True:
        time = input('Enter 10km run time: ')
        if time == '':
            break
        else:
            time = int(time)
            total_list.append(time)

    runs = 0
    total = 0  

    for run in total_list:
        total += run 
        runs += 1

    avg = total / runs 
    
    print(f'Average of {avg}, over {runs} runs!')



run_timing()