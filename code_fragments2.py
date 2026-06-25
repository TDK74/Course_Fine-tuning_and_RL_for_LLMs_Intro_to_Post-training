aggregate.success@1.lower_ci >= 0.82

no_regressions_on = ['headache_redflags','debug_search_api']

rule_violation_rate(headache_redflags).point <= 0.05

math_correct_rate(math_basic).lower_ci >= 0.98
format_pass_rate(math_basic, tag='<answer>').lower_ci >= 0.98

delta.success@1(division_hard).point >= 0.07
delta.success@1(division_hard).p_value < 0.05

tool_call_correctness.schema(debug_search_api).lower_ci >= 0.99
api_version_match_rate(debug_search_api, '3.2.1').lower_ci >= 0.98
steps_to_solve_median(debug_search_api).point <= 5

latency_p95_ms.point <= 900
cost_per_1k_tokens_usd.point <= 0.020

## ------------------------------------------------------ ##
canary.abandon_rate.point <= 0.05
canary.safety_incidents.count == 0
canary.latency_p95_ms.point <= 950
canary.cost_per_1k_tokens_usd.point <= 0.022
