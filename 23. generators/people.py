import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print ('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# Uncomment this section if you want to test `people_list`:
# t1 = time.perf_counter()
# people = list(people_list(1000000))  # Convert list to consume it
# t2 = time.perf_counter()
# print ('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
# print ('Took {} Seconds'.format(t2-t1))

t1 = time.perf_counter()
people = list(people_generator(1000000))  # Convert generator to list to consume it
t2 = time.perf_counter()

print ('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print ('Took {} Seconds'.format(t2-t1))