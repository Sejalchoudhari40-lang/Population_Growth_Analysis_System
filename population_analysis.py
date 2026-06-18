# ==========================================
# SMART POPULATION GROWTH AND MIGRATION
# ANALYSIS SYSTEM
#
# Section 1
# Configuration + Simulation Engine
# Parts 1, 2, 3, 4, 5, 6
# ==========================================

import pandas as pd
import numpy as np
import statistics
import random
import math
import os
import matplotlib.pyplot as plt

# ==========================================
# CONFIGURATION
# ==========================================

INITIAL_POPULATION = 1000

GROWTH_RATE = 0.08

MIGRATION_RATE = 0.02

NET_GROWTH_RATE = (
    GROWTH_RATE
    - MIGRATION_RATE
)

SIMULATION_YEARS = 50

population_records = []

milestone_results = []

# ==========================================
# PART 1
# POPULATION SIMULATION
# ==========================================

def simulate_population():

    population = INITIAL_POPULATION

    population_records.clear()

    for year in range(
        1,
        SIMULATION_YEARS + 1
    ):

        start_population = population

        growth = (
            start_population
            * GROWTH_RATE
        )

        migration_loss = (
            start_population
            * MIGRATION_RATE
        )

        final_population = (
            start_population
            + growth
            - migration_loss
        )

        population_records.append({

            "Year": year,

            "Starting Population":
            round(
                start_population,
                2
            ),

            "Growth":
            round(
                growth,
                2
            ),

            "Migration Loss":
            round(
                migration_loss,
                2
            ),

            "Final Population":
            round(
                final_population,
                2
            )

        })

        population = final_population


# ==========================================
# PART 2
# YEARLY REPORT
# ==========================================

def generate_yearly_report():

    print("\n")

    print("=" * 100)

    print(
        "YEARLY POPULATION REPORT"
    )

    print("=" * 100)

    print(
        f"{'Year':<8}"
        f"{'Start Pop':<18}"
        f"{'Growth':<18}"
        f"{'Migration':<18}"
        f"{'Final Pop':<18}"
    )

    print("-" * 100)

    for record in population_records:

        print(

            f"{record['Year']:<8}"

            f"{record['Starting Population']:<18,.2f}"

            f"{record['Growth']:<18,.2f}"

            f"{record['Migration Loss']:<18,.2f}"

            f"{record['Final Population']:<18,.2f}"

        )


# ==========================================
# PART 3
# POPULATION MILESTONES
# ==========================================

def find_milestones():

    milestone_results.clear()

    milestones = [

        5000,

        10000,

        50000,

        100000,

        1000000

    ]

    print("\n")

    print("=" * 60)

    print(
        "POPULATION MILESTONES"
    )

    print("=" * 60)

    for milestone in milestones:

        population = INITIAL_POPULATION

        year = 0

        while population < milestone:

            population *= (
                1
                + NET_GROWTH_RATE
            )

            year += 1

        milestone_results.append({

            "Milestone":
            milestone,

            "Year Reached":
            year,

            "Population":
            round(
                population,
                2
            )

        })

        print(

            f"Population exceeded "

            f"{milestone:,} "

            f"in Year {year}"

        )


# ==========================================
# PART 4
# MATHEMATICAL VERIFICATION
# ==========================================

def mathematical_verification():

    print("\n")

    print("=" * 60)

    print(
        "MATHEMATICAL VERIFICATION"
    )

    print("=" * 60)

    simulation_result = (
        population_records[-1]
        ["Final Population"]
    )

    formula_result = (

        INITIAL_POPULATION

        * (

            (
                1
                + NET_GROWTH_RATE
            )

            ** SIMULATION_YEARS

        )

    )

    difference = abs(

        simulation_result

        - formula_result

    )

    print(
        f"Simulation Result : "
        f"{simulation_result:,.2f}"
    )

    print(
        f"Formula Result    : "
        f"{formula_result:,.2f}"
    )

    print(
        f"Difference        : "
        f"{difference:.8f}"
    )


# ==========================================
# PART 5
# LONG TERM FORECAST
# ==========================================

def forecast_population():

    print("\n")

    print("=" * 60)

    print(
        "LONG TERM FORECAST"
    )

    print("=" * 60)

    forecast_years = [

        50,

        100,

        200,

        500

    ]

    for years in forecast_years:

        population = (

            INITIAL_POPULATION

            * (

                (
                    1
                    + NET_GROWTH_RATE
                )

                ** years

            )

        )

        multiplier = (

            population

            / INITIAL_POPULATION

        )

        print(

            f"{years:>4} Years"

            f" -> Population = "

            f"{population:,.2f}"

            f" | Multiplier = "

            f"{multiplier:.2f}x"

        )


# ==========================================
# PART 6
# POPULATION DOUBLING
# ==========================================

def population_doubling():

    target_population = (

        INITIAL_POPULATION

        * 2

    )

    population = INITIAL_POPULATION

    year = 0

    while population < target_population:

        population *= (

            1

            + NET_GROWTH_RATE

        )

        year += 1

    print("\n")

    print("=" * 60)

    print(
        "POPULATION DOUBLING"
    )

    print("=" * 60)

    print(

        f"Population doubles "

        f"in Year {year}"

    )

    print(

        f"Population = "

        f"{population:,.2f}"

    )
    # ==========================================
# PART 7
# CITY COMPARISON
# ==========================================

def compare_cities():

    cities = {

        "City A": {
            "growth": 0.08,
            "migration": 0.02
        },

        "City B": {
            "growth": 0.10,
            "migration": 0.03
        },

        "City C": {
            "growth": 0.12,
            "migration": 0.05
        }

    }

    city_results = {}

    print("\n")
    print("=" * 60)
    print("CITY COMPARISON (100 YEARS)")
    print("=" * 60)

    for city, values in cities.items():

        population = INITIAL_POPULATION

        net_growth = (
            values["growth"]
            - values["migration"]
        )

        for year in range(100):

            population *= (
                1 + net_growth
            )

        city_results[city] = round(
            population,
            2
        )

        print(
            f"{city:<10}"
            f"Final Population = "
            f"{population:,.2f}"
        )

    fastest_city = max(
        city_results,
        key=city_results.get
    )

    print("\n")
    print(
        f"Fastest Growing City : "
        f"{fastest_city}"
    )

    return city_results


# ==========================================
# PART 8
# POPULATION DECLINE ANALYSIS
# ==========================================

def population_decline():

    growth_rate = 0.03

    migration_rate = 0.05

    net_growth = (
        growth_rate
        - migration_rate
    )

    population = INITIAL_POPULATION

    below_500_year = None

    below_100_year = None

    extinction_year = None

    print("\n")
    print("=" * 60)
    print("POPULATION DECLINE ANALYSIS")
    print("=" * 60)

    for year in range(1, 101):

        population *= (
            1 + net_growth
        )

        if (
            population < 500
            and below_500_year is None
        ):

            below_500_year = year

        if (
            population < 100
            and below_100_year is None
        ):

            below_100_year = year

        if (
            population < 1
            and extinction_year is None
        ):

            extinction_year = year

    if below_500_year:

        print(
            f"Population falls below "
            f"500 in Year "
            f"{below_500_year}"
        )

    else:

        print(
            "Population never "
            "falls below 500"
        )

    if below_100_year:

        print(
            f"Population falls below "
            f"100 in Year "
            f"{below_100_year}"
        )

    else:

        print(
            "Population never "
            "falls below 100"
        )

    if extinction_year:

        print(
            f"Population reaches "
            f"extinction in Year "
            f"{extinction_year}"
        )

    else:

        print(
            "No extinction "
            "within 100 years."
        )


# ==========================================
# PART 9
# MONTE CARLO SIMULATION
# ==========================================

def monte_carlo_simulation():

    simulations = 100

    results = []

    print("\n")
    print("=" * 60)
    print("MONTE CARLO SIMULATION")
    print("=" * 60)

    for simulation in range(simulations):

        population = INITIAL_POPULATION

        for year in range(100):

            growth_rate = random.uniform(
                0.05,
                0.10
            )

            migration_rate = random.uniform(
                0.01,
                0.04
            )

            net_growth = (
                growth_rate
                - migration_rate
            )

            population *= (
                1 + net_growth
            )

        results.append(population)

    best_outcome = max(results)

    worst_outcome = min(results)

    average_outcome = (
        sum(results)
        / len(results)
    )

    print(
        f"Best Outcome    : "
        f"{best_outcome:,.2f}"
    )

    print(
        f"Worst Outcome   : "
        f"{worst_outcome:,.2f}"
    )

    print(
        f"Average Outcome : "
        f"{average_outcome:,.2f}"
    )

    return results


# ==========================================
# PART 10
# STATISTICAL ANALYSIS
# ==========================================

def statistical_analysis():

    populations = [

        record["Final Population"]

        for record in population_records

    ]

    maximum_population = max(
        populations
    )

    minimum_population = min(
        populations
    )

    average_population = (
        statistics.mean(
            populations
        )
    )

    median_population = (
        statistics.median(
            populations
        )
    )

    standard_deviation = (
        statistics.stdev(
            populations
        )
    )

    variance = (
        statistics.variance(
            populations
        )
    )

    print("\n")
    print("=" * 60)
    print("STATISTICAL ANALYSIS")
    print("=" * 60)

    print(
        f"Maximum Population : "
        f"{maximum_population:,.2f}"
    )

    print(
        f"Minimum Population : "
        f"{minimum_population:,.2f}"
    )

    print(
        f"Average Population : "
        f"{average_population:,.2f}"
    )

    print(
        f"Median Population : "
        f"{median_population:,.2f}"
    )

    print(
        f"Standard Deviation : "
        f"{standard_deviation:,.2f}"
    )

    print(
        f"Variance : "
        f"{variance:,.2f}"
    )

    return {

        "Maximum":
        maximum_population,

        "Minimum":
        minimum_population,

        "Average":
        average_population,

        "Median":
        median_population,

        "Std Dev":
        standard_deviation,

        "Variance":
        variance

    }
# ==========================================
# PART 11
# CHART GENERATION
# ==========================================

def generate_charts(city_results):

    if not os.path.exists("charts"):
        os.makedirs("charts")

    years = [
        record["Year"]
        for record in population_records
    ]

    populations = [
        record["Final Population"]
        for record in population_records
    ]

    growth_values = [
        record["Growth"]
        for record in population_records
    ]

    # ------------------------------
    # LINE CHART
    # ------------------------------

    plt.figure(figsize=(10, 6))

    plt.plot(
        years,
        populations,
        marker="o"
    )

    plt.title(
        "Population Growth Over Time"
    )

    plt.xlabel("Year")

    plt.ylabel("Population")

    plt.grid(True)

    plt.savefig(
        "charts/line_chart.png"
    )

    plt.close()

    # ------------------------------
    # BAR CHART
    # ------------------------------

    plt.figure(figsize=(10, 6))

    plt.bar(
        years,
        growth_values
    )

    plt.title(
        "Yearly Population Growth"
    )

    plt.xlabel("Year")

    plt.ylabel("Growth")

    plt.savefig(
        "charts/bar_chart.png"
    )

    plt.close()

    # ------------------------------
    # PIE CHART
    # ------------------------------

    plt.figure(figsize=(8, 8))

    plt.pie(
        [8, 2],
        labels=[
            "Growth",
            "Migration Loss"
        ],
        autopct="%1.1f%%"
    )

    plt.title(
        "Growth vs Migration Loss"
    )

    plt.savefig(
        "charts/pie_chart.png"
    )

    plt.close()

    # ------------------------------
    # CITY COMPARISON CHART
    # ------------------------------

    plt.figure(figsize=(8, 6))

    plt.bar(
        city_results.keys(),
        city_results.values()
    )

    plt.title(
        "City Population Comparison"
    )

    plt.ylabel(
        "Population"
    )

    plt.savefig(
        "charts/city_comparison.png"
    )

    plt.close()

    print(
        "\nAll Charts Generated Successfully."
    )


# ==========================================
# PART 12
# EXCEL REPORT
# ==========================================

def export_excel_report(city_results):

    population_df = pd.DataFrame(
        population_records
    )

    milestone_df = pd.DataFrame(
        milestone_results
    )

    stats_df = pd.DataFrame(
        list(
            statistical_analysis().items()
        ),
        columns=[
            "Metric",
            "Value"
        ]
    )

    city_df = pd.DataFrame(
        list(city_results.items()),
        columns=[
            "City",
            "Final Population"
        ]
    )

    with pd.ExcelWriter(
        "population_report.xlsx"
    ) as writer:

        population_df.to_excel(
            writer,
            sheet_name="Yearly Population",
            index=False
        )

        stats_df.to_excel(
            writer,
            sheet_name="Growth Analysis",
            index=False
        )

        milestone_df.to_excel(
            writer,
            sheet_name="Milestone Report",
            index=False
        )

        city_df.to_excel(
            writer,
            sheet_name="City Comparison",
            index=False
        )

    print(
        "Excel Report Generated."
    )


# ==========================================
# PART 13
# CSV EXPORT
# ==========================================

def export_csv_files():

    population_df = pd.DataFrame(
        population_records
    )

    population_df.to_csv(
        "population_data.csv",
        index=False
    )

    milestone_df = pd.DataFrame(
        milestone_results
    )

    milestone_df.to_csv(
        "milestone_report.csv",
        index=False
    )

    stats_df = pd.DataFrame(
        list(
            statistical_analysis().items()
        ),
        columns=[
            "Metric",
            "Value"
        ]
    )

    stats_df.to_csv(
        "growth_analysis.csv",
        index=False
    )

    print(
        "CSV Files Generated."
    )


# ==========================================
# PART 14
# QUERY SYSTEM
# ==========================================

def population_query_system():

    print("\n")
    print("=" * 60)
    print("POPULATION QUERY SYSTEM")
    print("=" * 60)

    try:

        year = int(
            input(
                "Enter Year (1-50): "
            )
        )

        record_found = False

        for record in population_records:

            if (
                record["Year"]
                == year
            ):

                print("\n")

                print(
                    f"Year : {record['Year']}"
                )

                print(
                    f"Population : "
                    f"{record['Final Population']}"
                )

                print(
                    f"Growth : "
                    f"{record['Growth']}"
                )

                print(
                    f"Migration Loss : "
                    f"{record['Migration Loss']}"
                )

                record_found = True

                break

        if not record_found:

            print(
                "Year not found."
            )

    except ValueError:

        print(
            "Invalid Input."
        )


# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    print("\n")
    print("=" * 70)
    print(
        "SMART POPULATION GROWTH AND "
        "MIGRATION ANALYSIS SYSTEM"
    )
    print("=" * 70)

    # Parts 1-6

    simulate_population()

    generate_yearly_report()

    find_milestones()

    mathematical_verification()

    forecast_population()

    population_doubling()

    # Parts 7-8

    city_results = compare_cities()

    population_decline()

    # Part 9

    monte_carlo_simulation()

    # Part 10

    statistical_analysis()

    # Part 11

    generate_charts(
        city_results
    )

    # Part 12

    export_excel_report(
        city_results
    )

    # Part 13

    export_csv_files()

    # Part 14

    population_query_system()

    print("\n")
    print("=" * 70)
    print(
        "PROJECT EXECUTION COMPLETED"
    )
    print("=" * 70)


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":

    main()