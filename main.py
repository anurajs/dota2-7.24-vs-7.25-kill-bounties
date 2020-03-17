victim_level = 3
victim_networth = 800
comeback = 0
victim_streak = 0
surrounding_heroes = 1



def old_aoe(n,poor,ranking,comeback,viclvl,vicnw):
  x=0
  if n ==1:
    x= poor*ranking*(126 + 4.5*viclvl +comeback*(vicnw*.026 +70)/1)
  elif n==2:
    x= poor*ranking*(63 +  3.6*viclvl +comeback*(vicnw*.026 +70)/2)
  elif n==3:
    x= poor*ranking*(31.5 + 2.7*viclvl +comeback*(vicnw*.026 +70)/3)
  elif n==4:
    x= poor*ranking*(22.5 + 1.8*viclvl +comeback*(vicnw*.026 +70)/4)
  else:
    x= poor*ranking*(18 + 0.9*viclvl +comeback*(vicnw*.026 +70)/5)
  return x

def new_aoe(n, vicnw):
  return (50+vicnw*0.03)/n

def kill_old(streak,viclvl):
  sv = 0
  if streak == 3:
    sv = 60
  elif streak == 4:
    sv = 120
  elif streak == 5:
    sv = 180
  elif streak == 6:
    sv = 240
  elif streak == 7:
    sv = 300
  elif streak == 8:
    sv = 360
  elif streak == 9:
    sv = 420
  elif streak >= 10:
    sv = 480
  return sv + 110 + (viclvl * 8)

def kill_new(streak,viclvl):
  sv = 0
  if streak == 3:
    sv = 200
  elif streak == 4:
    sv = 270
  elif streak == 5:
    sv = 340
  elif streak == 6:
    sv = 410
  elif streak == 7:
    sv = 480
  elif streak == 8:
    sv = 550
  elif streak == 9:
    sv = 629
  elif streak >= 10:
    sv = 690
  return sv + 110 + (viclvl * 8)

print(int(kill_old(victim_streak,victim_level) + old_aoe(surrounding_heroes,0.6,1.6,comeback,victim_level,victim_networth))," gold if you are the richest on your team, the victim is the richest on their team - old formula")

print(int(kill_old(victim_streak,victim_level) + old_aoe(surrounding_heroes,1.2,1.6,comeback,victim_level,victim_networth))," gold if you are the poorest on your team, the victim is the richest on their team - old formula")

print(int(kill_old(victim_streak,victim_level) + old_aoe(surrounding_heroes,0.6,0.4,comeback,victim_level,victim_networth))," gold if you are the richest on your team, the victim is the poorest on their team - old formula")

print(int(kill_old(victim_streak,victim_level) + old_aoe(surrounding_heroes,1.2,0.4,comeback,victim_level,victim_networth))," gold if you are the poorest on your team, the victim is the poorest on their team - old formula")

print(int(kill_new(victim_streak,victim_level) + new_aoe(surrounding_heroes,victim_networth)), "Gold for new formula")