def fault_probability(PROB__hist_var_4_sen2_sensor_failure_mode_is_deltaout_TRUE=1.000000e-03, PROB__hist_var_5_sen1_sensor_failure_mode_is_deltaout_TRUE=1.000000e-03, PROB__hist_var_2_batt2_battery_failure_mode_is_rampdown_TRUE=1.000000e-01, PROB__hist_var_3_batt1_battery_failure_mode_is_rampdown_TRUE=1.000000e-01):
    EXPR_1 = PROB__hist_var_4_sen2_sensor_failure_mode_is_deltaout_TRUE
    EXPR_2 = PROB__hist_var_5_sen1_sensor_failure_mode_is_deltaout_TRUE
    EXPR_3 = 1
    EXPR_4 = EXPR_3 - EXPR_2
    EXPR_5 = PROB__hist_var_3_batt1_battery_failure_mode_is_rampdown_TRUE
    EXPR_6 = EXPR_4 * EXPR_5
    EXPR_7 = EXPR_2 + EXPR_6
    EXPR_8 = EXPR_1 * EXPR_7
    EXPR_9 = EXPR_3 - EXPR_1
    EXPR_10 = PROB__hist_var_2_batt2_battery_failure_mode_is_rampdown_TRUE
    EXPR_11 = EXPR_2 * EXPR_10
    EXPR_12 = EXPR_10 * EXPR_5
    EXPR_13 = EXPR_4 * EXPR_12
    EXPR_14 = EXPR_11 + EXPR_13
    EXPR_15 = EXPR_9 * EXPR_14
    EXPR_16 = EXPR_8 + EXPR_15
    prob = EXPR_16
    return prob

if __name__ == '__main__':
    p = fault_probability()
    print("Default probability of TLE is: %e\n" % p)
