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

    avg = 0
    total = 0  

    for run in total_list:
        total += run 
        avg += 1

    average = total / avg 
    
    print(f'Average of {average}, over {avg} runs!')



run_timing()