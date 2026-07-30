#homework completion tracker

#step1
total_homework=4
original_count=total_homework
print(f"you have {original_count} homework task to finish today!\n")

#step2
completed_count=0
tak_num=1

#part3
while tak_num<=total_homework:

    #part4
    if tak_num == 1:
       next_task="math homework"
    elif tak_num == 2:
       next_task="science homework"
    elif tak_num == 3:
       next_task="history homework"
    else:
       next_task="coding homework"

    answer=input(f"have you completed {next_task}? (yes/no): ")

    #part5
    if answer == "yes":
        completed_count+=1
        tak_num += 1
        print("great job task completed")
    else:
        print("finish it and check it again") 

    #part6
    print("homework task remaining:", total_homework - completed_count)      
    print()

    #part7
    print("====ALL HOMEWORK COMPLETE====")
    print("great work finishing your homework today!\n")

    #part8
    print("Now lets safley peek at an infinite loop...")
    test_value = 0
    safe_counter = 0

    while test_value <= 0:
        print("this condition never changes,so it will go forever")
        safe_counter += 1

        if safe_counter == 3:
           print("(stopping here on purpose a real ifinite loop never stops!)")
           break

    #part9
    print("\n======== HOMEWORK COMPLETION SUMMARY ========")
    print("homework assiagned today:", original_count)
    print("homework completed today:",completed_count)
    print("homework remaining today:", total_homework - completed_count)
    print("============================================================")
