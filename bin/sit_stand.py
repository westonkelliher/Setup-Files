#!/usr/bin/python
import subprocess as sp
import time

last_time = time.time()

def tprint(t):
  t = int(t)
  secs = t % 60
  t /= 60
  t = int(t)
  mins = t % 60
  t /= 60
  t = int(t)
  hours = t % 24
  print(str(hours)+':'+str(mins)+'.'+str(secs))

  
def between_modulus(n, m, old_time, new_time):
  time_to_pass = old_time - (old_time % m) + n
  if time_to_pass < old_time:
    time_to_pass += m
  return new_time > time_to_pass


def has_passed_nth_second(n, last_time):
  has_passed = between_modulus(n, 60, last_time, time.time())
  return has_passed

def has_passed_nth_minute(n, last_time):
  has_passed = between_modulus(n*60, 60*60, last_time, time.time())
  return has_passed

def has_passed_nth_hour_PST(n, last_time):
  n -= 17
  if n < 0:
    n += 24
  has_passed = between_modulus(n*60*60, 60*60*24, last_time, time.time())
  return has_passed



def my_notify(text, width=105):
  sp.call(['zenity', '--info', '--width='+str(width), '--title=SitStand',
           '--text='+str(text)])
  

my_notify('Clock in')

while True:
  t = time.time() - 10
    
  if has_passed_nth_minute(0, t):
    my_notify('Sit')

  if has_passed_nth_minute(40, t):
    my_notify('Stand')

  if has_passed_nth_hour_PST(22, t):
    my_notify('One hour left')

  time.sleep(10)

