import pandas as pd

data = [
    ["Field", "Value"],
    ["Date", "22 May 2026, 15:38"],
    ["Amount", "N10,000.00"],
    ["Status", "Success"],
    ["Sender", "Amu Frank Okepede"],
    ["Receiver", "Frank Okepede Amu"],
    ["Account number", "9041887840"],
    ["Receiving bank", "Opay"],
    ["Reference", "000013260522153814000045164771"]
]

df = pd.DataFrame(data[1:], columns=data[0])
df.to_excel("gtco_cleaned.xlsx", index=False)

print("Done! Your GTCO cleaned Excel is ready")
print(df)