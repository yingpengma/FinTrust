# Data

As previously mentioned, we have divided the earnings call dataset into mutually exclusive train/validation/test sets in a 7:1:2 ratio based on chronological order, resulting in a test set containing 113 samples. This test set is stored in a file named "earnings_call.npy", where each row contains three columns: the date (year/month/day) of the earnings call, the associated company, and the conference record. 

Additionally, we have obtained the stock price movements 3, 7, 15, and 30 days after each earnings call, represented by binary values 0 and 1 (0 indicates a decrease in stock price, while 1 indicates an increase). These movements are saved in four separate files named "stock_movement_3days.npy", and so on.

For example, to merge the earnings call data with the stock price movements 3 days after each call, we combine "earnings_call.npy" with "stock_movement_3days.npy" to obtain "earnings_call_3days.npy". We can then apply four types of consistency transformations to this data to obtain "neg_earnings_call_3days.npy", "sym_earnings_call_3days.npy", "tra_earnings_call_3days.npy", and "add_earnings_call_3days.npy".

