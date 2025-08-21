module SavingsAccount
  INTEREST_RATE_LESS_THAN_1000 = 0.5
  INTEREST_RATE_LESS_THAN_5000 = 1.621
  INTEREST_RATE_GREATER_THAN_5000 = 2.475
  INTEREST_RATE_NEGATIVE_BALANCE = 3.213

  def self.interest_rate(balance)
    if balance.negative?
      INTEREST_RATE_NEGATIVE_BALANCE
    elsif balance < 1000
      INTEREST_RATE_LESS_THAN_1000
    elsif balance < 5000
      INTEREST_RATE_LESS_THAN_5000
    else
      INTEREST_RATE_GREATER_THAN_5000
    end
  end

  def self.annual_balance_update(balance)
    raise 'Please implement the SavingsAccount.annual_balance_update method'
  end

  def self.years_before_desired_balance(current_balance, desired_balance)
    raise 'Please implement the SavingsAccount.years_before_desired_balance method'
  end
end
