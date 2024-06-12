import streamlit as st

def american_to_decimal(odds):
    if odds > 0:
        return 1 + (odds / 100)
    else:
        return 1 + (100 / abs(odds))

def calculate_arbitrage(odds_team1, odds_team2, wager_team1, wager_team2):
    total_wager = wager_team1 + wager_team2
    potential_win_team1 = wager_team1 * odds_team1
    potential_win_team2 = wager_team2 * odds_team2
    profit_team1 = potential_win_team1 - total_wager
    profit_team2 = potential_win_team2 - total_wager
    return profit_team1, profit_team2

def calculate_bookmaker_profit(odds_team1, odds_team2):
    implied_prob_team1 = 1 / odds_team1
    implied_prob_team2 = 1 / odds_team2
    total_implied_prob = implied_prob_team1 + implied_prob_team2
    bookmaker_profit = (total_implied_prob - 1) * 100
    return bookmaker_profit

def calculate_cumulative_profit(profit_team1, profit_team2):
    cumulative_profit_team1 = profit_team1
    cumulative_profit_team2 = profit_team2
    return cumulative_profit_team1, cumulative_profit_team2

def check_arbitrage(odds_team1, odds_team2):
    arbitrage_condition = (1 / odds_team1) + (1 / odds_team2)
    return arbitrage_condition < 1

st.title("Arbitrage Betting Calculator")

# Add a banner image
st.image("https://media.npr.org/assets/img/2022/06/14/ellingson_corrected_wide-da0efa6b9cc12438a4cc0c96b1ba0fb01c9de7b1.jpg", use_column_width=True)
# Centered caption
st.markdown('<p style="text-align: center;">Kyle Ellingson for NPR</p>', unsafe_allow_html=True)

st.header("Enter the odds and wager amounts")

team1 = st.text_input("Team 1 Name", value="Team 1")
team2 = st.text_input("Team 2 Name", value="Team 2")

col1, col2 = st.columns(2)

with col1:
    odds_team1_american = st.number_input(f"American Odds for {team1}", value=110)
    wager_team1 = st.number_input(f"Wager Amount on {team1}", min_value=0.0, value=50.0)

with col2:
    odds_team2_american = st.number_input(f"American Odds for {team2}", value=-115)
    wager_team2 = st.number_input(f"Wager Amount on {team2}", min_value=0.0, value=50.0)

# Convert American odds to Decimal odds
odds_team1 = american_to_decimal(odds_team1_american)
odds_team2 = american_to_decimal(odds_team2_american)

if st.button("Calculate"):
    profit_team1, profit_team2 = calculate_arbitrage(odds_team1, odds_team2, wager_team1, wager_team2)
    bookmaker_profit = calculate_bookmaker_profit(odds_team1, odds_team2)
    cumulative_profit_team1, cumulative_profit_team2 = calculate_cumulative_profit(profit_team1, profit_team2)
    arbitrage_exists = check_arbitrage(odds_team1, odds_team2)
    
    st.subheader("Results")
    
    st.markdown(f"### {team1} vs {team2}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"#### {team1}")
        st.write(f"Potential Profit if {team1} wins: ${profit_team1:.2f}")
        st.write(f"Cumulative Profit/Loss if {team1} wins: ${cumulative_profit_team1:.2f}")
    
    with col2:
        st.markdown(f"#### {team2}")
        st.write(f"Potential Profit if {team2} wins: ${profit_team2:.2f}")
        st.write(f"Cumulative Profit/Loss if {team2} wins: ${cumulative_profit_team2:.2f}")
    
    st.markdown(f"#### Bookmaker's Profit Margin: {bookmaker_profit:.2f}%")
    
    if arbitrage_exists:
        st.markdown("#### Arbitrage Opportunity: **Yes**")
    else:
        st.markdown("#### Arbitrage Opportunity: **No**")

# Add author name to footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: small;
    }
    </style>
    <div class="footer">
        Made with ♥︎ by Amitabha Dey
    </div>
    """,
    unsafe_allow_html=True
)