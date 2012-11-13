circ_km = 0.0021
circ_m = circ_km * 1000
body_eff = 0.24
train_eff = 0.95
mass_kg = 2.5
joules_to_kcal = 0.000239
crank_radius_cm = 17.78
wheel_radius_cm = 33.4

#forward_teeth = [ -1, -1, 48.0 ]
#rear_teeth = [ -1, -1, -1, -1, -1, -1, -1, 12.0 ]

def kcal_required( joules ):
  return joules / body_eff * joules_to_kcal

def joules_required( speed_ms, resistance ):
  return -accel(speed_ms,resistance) * mass_kg * circ_m / train_eff

#def joules_2( speed_ms, resistance ):
#  return -accel(speed_ms,resistance) * mass_kg * gain_ratio( 3, 8 ) * (crank_radius_cm/100*2*3.14159) / train_eff

#def total_j( dist_m, time_s ):
#  vel_ms = dist_m/time_s
#  return -accel(vel_ms,8) * mass_kg * dist_m / train_eff

#def gain_ratio( forward, backward ):
#   return (wheel_radius_cm/crank_radius_cm) * (forward_teeth[forward-1]/rear_teeth[backward-1])

def accel( speed, resistance ):
  if resistance == 8:
    return -0.26796*speed-1.05192
  if resistance == 3:
    return -0.18*speed-0.25
