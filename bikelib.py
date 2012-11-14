circ_km = 0.0021
circ_m = circ_km * 1000
body_eff = 0.24
train_eff = 0.95
mass_kg = 2.5
joules_to_kcal = 0.000239

def kcal_required( joules ):
  return joules / body_eff * joules_to_kcal

def joules_required( speed_ms, resistance ):
  return -accel(speed_ms,resistance) * mass_kg * circ_m / train_eff

def accel( speed, resistance ):
  if resistance == 8:
    return -0.26796*speed-1.05192
  if resistance == 3:
    return -0.18*speed-0.25
