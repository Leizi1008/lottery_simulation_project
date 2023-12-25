from lottery_simulation import simulate_lottery
from lottery_utils import save_results_to_csv, save_results_to_txt
from history_analyzer import analyze_history

def main():
    # 分析历史数据
    history_stats = analyze_history('../data/historical_lottery_data.csv')
    print("历史数据分析结果:", history_stats)

    # 进行模拟
    simulation_results = simulate_lottery()

    # 保存结果到CSV
    save_results_to_csv(simulation_results, '../results/simulation_output.csv')
    
    # 保存结果到TXT
    save_results_to_txt(simulation_results, '../results/simulation_output.txt')

    print("模拟完成，结果已保存。")

if __name__ == "__main__":
    main()
