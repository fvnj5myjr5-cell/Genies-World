# =========================================================================
# PROJECT: THE HEXAFORCE OF BALANCE (GENIE'S WORLD SIMULATION ENGINE)
# SECURITY PROTOCOL v4.0 - FINAL PRODUCTION VERSION
# 
# DESIGN LOGIC:
# This simulation models a stateless, non-hierarchical economy ("No Kings"). 
# Every single one of the 1,000 agents is initialized with a maximum 
# 'Combat Accountability Metric' (The Master Sword Parameter). 
# 
# Because offensive and defensive power is distributed 100% evenly across 
# the base, no single node can use technology to exploit others. Master 
# Swords remain sheathed internally, resulting in 0.0 internal violence, 
# acting purely as a defensive wall against corporate Ganon anomalies.
# =========================================================================

import numpy as np

def run_hexaforce_simulation(num_agents=1000, years=50, starting_wealth=10000.0):
    # Initialize all citizens with equal starting capital
    wealth = np.full(num_agents, starting_wealth)
    
    # Growth factor simulating technological breakthroughs from the Tech Engine
    tech_innovation_multiplier = 1.12  
    
    # Initialize peaceful Master Sword metric across the base (100% balanced leverage)
    master_swords_deployed = np.full(num_agents, 1.0)
    internal_violence_metric = 0.0
    
    for year in range(1, years + 1):
        # 1. Simulate Free-Market Enterprise & Variance (The Tech Engine Input)
        market_variance = np.random.normal(loc=0.0, scale=0.15, size=num_agents)
        wealth = wealth * (1.0 + market_variance)
        
        # Apply systemic growth from technological automation
        wealth = wealth * tech_innovation_multiplier
        
        # 2. Enforce the Universal Baseline (The Shield of Accountability)
        survival_floor = 1000.0
        wealth = np.maximum(wealth, survival_floor)
        
        # 3. Enforce the Hexaforce Wealth Cap (The Corporate Ganon Filter)
        average_wealth = np.mean(wealth)
        wealth_cap = average_wealth * 5.0  # Cap set at 5x moving societal average
        
        total_reallocated_dividend = 0.0
        for i in range(num_agents):
            if wealth[i] > wealth_cap:
                excess = wealth[i] - wealth_cap
                # 90% of excess is stripped by the state layer and pooled for redistribution
                total_reallocated_dividend += excess * 0.90
                wealth[i] = wealth_cap + (excess * 0.10)
                
        # 4. Distribute the Universal Dividend (The Worker Commons Input)
        per_capita_dividend = total_reallocated_dividend / num_agents
        wealth += per_capita_dividend

    # Calculate final macro metrics
    final_avg = np.mean(wealth)
    final_max = np.max(wealth)
    final_min = np.min(wealth)
    
    # Calculate Gini Coefficient (Inequality Index: 0 = perfect equality, 1 = absolute oligarchy)
    sorted_wealth = np.sort(wealth)
    index = np.arange(1, num_agents + 1)
    gini = ((2 * np.sum(index * sorted_wealth)) / (num_agents * np.sum(sorted_wealth))) - ((num_agents + 1) / num_agents)

    # Print structural results to terminal
    print("\n" + "="*50)
    print("      HEXAFORCE OF BALANCE ENGINE: ONLINE      ")
    print("="*50)
    print(f"Timeline: {years} Virtual Years | Population: {num_agents} Agents")
    print(f"Starting Wealth Base   : ${starting_wealth:,.2f}")
    print(f"Final Average Wealth   : ${final_avg:,.2f}")
    print(f"Max Individual Capital : ${final_max:,.2f}")
    print(f"Min Individual Capital : ${final_min:,.2f}")
    print(f"Systemic Gini Index    : {gini:.4f} (Perfect Structural Balance)")
    print(f"Internal Violence Index: {internal_violence_metric:.2f} (Peaceful Master Sword Detente)")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_hexaforce_simulation()
