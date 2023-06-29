"""
Parameters for student clubs
"""


"""
Imports
"""

import sys

sys.path.append("src")

# Common assumptions
import utilities.assumptions.assumptions_baserates as adb

# Modify parameters for different robustness scenarios
import utilities.functions.robustness as fr

# Specifying distribution shape or magnitude of parameters
import squigglepy as sq
from squigglepy.numbers import K, M


"""
Specify parameters, building up from simple assumptions
"""

params_build_cost_and_participants = {
    # Cost
    "target_budget": 350 * K,
    "fixed_hours_labor": sq.to(300, 400),
    "average_wage": 60,
    "sd_variable_cost_students": 100,
    "sd_hours_labor": 30,
    "fixed_cost_other": sq.to(30 * K, 70 * K),
    "split_variable_cost_students": 0.95,  # effectively includes office space, organizer pay, etc.
    # Number of people
    "n_student_undergrad_scaling_parameter_gamma": 0.75,
    "n_student_undergrad_scaling_parameter_slope": 0.2,
    "n_student_undergrad_scaling_parameter_intercept": 3,
    "n_student_phd_scaling_parameter_gamma": 0.75,
    "n_student_phd_scaling_parameter_slope": 0.03,
    "n_student_phd_scaling_parameter_intercept": 0,
    "n_student_deterministic": False,
    # Pipeline and scientist-equivalence
    "p_pursue_ais": 0.02,  # mean 0.24
    "p_phd_given_pursue_ais": 1,
    "p_scientist_given_phd": 1,
    "p_professor_given_phd": 0,
    "p_engineer_given_phd": 0,
    "p_scientist_given_not_phd": 1,
    "p_professor_given_not_phd": 0,
    "p_engineer_given_not_phd": 0,
    "scientist_equivalent_professor": 1,
    "scientist_equivalent_engineer": 1,
    "scientist_equivalent_phd": 1,
    # Ability
    "ability_at_first_student_undergrad": 1,
    "ability_at_pivot_student_undergrad": 1,
    "ability_pivot_point_student_undergrad": 10,
    "ability_at_first_student_phd": 1,
    "ability_at_pivot_student_phd": 1,
    "ability_pivot_point_student_phd": 10,
    # Hours
    "hours_scientist_per_year": adb.hours_scientist_per_year,
    # Research avenue relevance
    "research_relevance_student_undergrad_via_phd": 1,
    "research_relevance_multiplier_after_phd_student_undergrad_via_phd": 1,
    "research_relevance_during_program_student_undergrad_via_phd": None,
    "research_relevance_student_undergrad_not_via_phd": 1,
    "research_relevance_during_program_student_undergrad_not_via_phd": None,
    "research_relevance_student_phd": 1,
    "research_relevance_multiplier_after_phd_student_phd": 1,
    "research_relevance_during_program_student_phd": None,
    # Productivity, staying in AI research, and time discounting
    "years_in_program_student_undergrad": 0,
    "years_in_program_student_phd": 0,
    "years_until_phd_undergrad": 2,
    "years_until_phd_phd": 3 - adb.years_in_phd,
    "years_in_phd": adb.years_in_phd,
    "research_discount_rate": 0,
    "slope_productivity_life_cycle": 0,
    "pivot_productivity_life_cycle": adb.pivot_productivity_life_cycle,
    "slope_staying_in_ai": 0,
    "pivot_staying_in_ai": adb.pivot_staying_in_ai,
    "end_staying_in_ai": 60,
    # Flags
    "student_phd": True,
}

additional_params_build_cost_and_participants_cf = {
    "p_pursue_ais": 0.01,
    "research_relevance_student_undergrad_via_phd": 0,
    "research_relevance_student_undergrad_not_via_phd": 0,
    "research_relevance_student_phd": 0,
}

params_build_cost_and_participants_cf = {
    **params_build_cost_and_participants,
    **additional_params_build_cost_and_participants_cf,
}

additional_params_build_pipeline_and_equivalence = {
    "p_pursue_ais": sq.beta(0.2 * 300, (1 - 0.2) * 300),
    "p_phd_given_pursue_ais": sq.beta(0.15 * 300, (1 - 0.15) * 300),
    "p_scientist_given_phd": adb.p_scientist_given_phd,
    "p_professor_given_phd": adb.p_professor_given_phd,
    "p_engineer_given_phd": adb.p_engineer_given_phd,
    "p_scientist_given_not_phd": sq.beta(0.15 * 300, (1 - 0.15) * 300),
    "p_engineer_given_not_phd": sq.beta(0.3 * 300, (1 - 0.3) * 300),
    "scientist_equivalent_professor": adb.scientist_equivalent_professor,
    "scientist_equivalent_engineer": adb.scientist_equivalent_engineer,
    "scientist_equivalent_phd": adb.scientist_equivalent_phd,
}

additional_params_build_pipeline_and_equivalence_cf = {
    "p_pursue_ais": sq.beta(0.1 * 300, (1 - 0.1) * 300),
}

params_build_pipeline_and_equivalence = {
    **params_build_cost_and_participants,
    **additional_params_build_pipeline_and_equivalence,
}

params_build_pipeline_and_equivalence_cf = {
    **params_build_pipeline_and_equivalence,
    **additional_params_build_cost_and_participants_cf,
    **additional_params_build_pipeline_and_equivalence_cf,
}

additional_params_build_relevance_and_ability = {
    "research_relevance_student_undergrad_via_phd": 3,
    "research_relevance_multiplier_after_phd_student_undergrad_via_phd": 0.7,
    "research_relevance_during_program_student_undergrad_via_phd": None,
    "research_relevance_student_undergrad_not_via_phd": 3,
    "research_relevance_during_program_student_undergrad_not_via_phd": None,
    "research_relevance_student_phd": 5,
    "research_relevance_multiplier_after_phd_student_phd": 1,
    "research_relevance_during_program_student_phd": 5,
    "ability_at_first_student_undergrad": 1.5,
    "ability_at_pivot_student_undergrad": 0.97,
    "ability_pivot_point_student_undergrad": 3,
    "ability_at_first_student_phd": 3,
    "ability_at_pivot_student_phd": 0.6,
    "ability_pivot_point_student_phd": 3,
}

additional_params_build_relevance_and_ability_cf = {
    "research_relevance_student_undergrad_via_phd": 0.3,
    "research_relevance_multiplier_after_phd_student_undergrad_via_phd": 0.7,
    "research_relevance_student_undergrad_not_via_phd": 0.3,
    "research_relevance_student_phd": 0.5,
    "research_relevance_multiplier_after_phd_student_phd": 1,
}

params_build_relevance_and_ability = {
    **params_build_cost_and_participants,
    **additional_params_build_pipeline_and_equivalence,
    **additional_params_build_relevance_and_ability,
}

params_build_relevance_and_ability_cf = {
    **params_build_relevance_and_ability,
    **additional_params_build_cost_and_participants_cf,
    **additional_params_build_pipeline_and_equivalence_cf,
    **additional_params_build_relevance_and_ability_cf,
}

additional_params_build_remaining_time_functions = {
    "research_discount_rate": adb.research_discount_rate,
    "slope_productivity_life_cycle": adb.slope_productivity_life_cycle,
    "slope_staying_in_ai": adb.slope_staying_in_ai,
}

additional_params_build_remaining_time_functions_cf = {}

params_build_remaining_time_functions = {
    **params_build_cost_and_participants,
    **additional_params_build_pipeline_and_equivalence,
    **additional_params_build_relevance_and_ability,
    **additional_params_build_remaining_time_functions,
}

params_build_remaining_time_functions_cf = {
    **params_build_remaining_time_functions,
    **additional_params_build_cost_and_participants_cf,
    **additional_params_build_pipeline_and_equivalence_cf,
    **additional_params_build_relevance_and_ability_cf,
    **additional_params_build_remaining_time_functions_cf,
}


"""
Default parameters
"""

params_mainline = params_build_remaining_time_functions
params_mainline_cf = params_build_remaining_time_functions_cf


"""
Dictionary of parameter dictionaries
"""

params = {
    "mainline": params_mainline,
    "mainline_cf": params_mainline_cf,
    "build_cost_and_participants": params_build_cost_and_participants,
    "build_cost_and_participants_cf": params_build_cost_and_participants_cf,
    "build_pipeline_and_equivalence": params_build_pipeline_and_equivalence,
    "build_pipeline_and_equivalence_cf": params_build_pipeline_and_equivalence_cf,
    "build_relevance_and_ability": params_build_relevance_and_ability,
    "build_relevance_and_ability_cf": params_build_relevance_and_ability_cf,
    "build_remaining_time_functions": params_build_remaining_time_functions,
    "build_remaining_time_functions_cf": params_build_remaining_time_functions_cf,
}


"""
Standard robustness checks
"""

checks = [
    "larger_difference_in_scientist_equivalence",
    "smaller_difference_in_scientist_equivalence",
    "larger_labor_costs",
    "smaller_labor_costs",
    "larger_fixed_costs",
    "smaller_fixed_costs",
    "larger_student_costs",
    "smaller_student_costs",
    "better_job_prospects",
    "worse_job_prospects",
]

params = fr.perform_robustness_checks(params, checks)
