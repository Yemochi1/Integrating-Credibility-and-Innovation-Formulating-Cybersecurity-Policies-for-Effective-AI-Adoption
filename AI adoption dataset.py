# this program is a dataset of AI adoption that show the barrier prioritization $ readiness ranking,frequency & weight, ranking, barrier priority,readiness leaderboard.
import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.max_colwidth', None)

barriers = [
    "Lack of Visibility on Benefits",
    "Integration Complexity & Incompatibility",
    "Technology Immaturity",
    "Security",
    "Lack of Strategic Vision",
    "Lack of Infrastructure",
    "Lack of Technical Expertise",
    "Lack of Usable Data",
    "Perceived Cost of Adoption",
    "Data Governance Issues",
    "Technology Trust Issues",
    "Regulatory Compliance"
]

cols = ["Paper_ID", "Paper_Name", "Year"] + barriers

table1_data = [
    ["T1-001", "Rawindaran et al.", 2021, "✓","✓","","✓","","","","","","","",""],
    ["T1-002", "Bresniker et al.", 2019, "✓","","","","","","","","","","","✓"],
    ["T1-003", "Sen et al.", 2022, "✓","✓","","✓","","","","","","","",""],
    ["T1-004", "Kant & Johannsen", 2022, "✓","✓","✓","✓","✓","✓","✓","✓","✓","","",""],
    ["T1-005", "Truong et al.", 2020, "✓","","","","","","","","","","",""],
    ["T1-006", "Kshetri", 2021, "✓","✓","✓","✓","","","","","","","","✓"],
    ["T1-007", "Taddeo", 2019, "","","","","","","","","","","✓",""],
    ["T1-008", "Bruschi & Diomede", 2023, "","","","","","","","","","✓","",""],
    ["T1-009", "Crowley & Filkins", 2022, "","","","","","","","","","✓","",""],
    ["T1-010", "Adebayo et al.", 2022, "","","","","✓","","","","","","",""],
    ["T1-011", "Wirkuttis & Klein", 2017, "","✓","","","✓","✓","✓","✓","✓","","",""],
    ["T1-012", "Sarker et al.", 2021, "","","✓","","","","✓","","","","",""],
    ["T1-013", "Garcia et al.", 2021, "✓","✓","✓","✓","","✓","✓","✓","✓","","✓",""],
    ["T1-014", "Taddeo et al.", 2019, "","","","","","","","","","✓","✓","✓"],
    ["T1-015", "Taddeo", 2021, "","","✓","","","✓","","","","✓","",""],
    ["T1-016", "Timmers", 2019, "","","","","","","","","","","✓",""],
    ["T1-017", "Samtani et al.", 2020, "","","✓","","","","","","","","",""],
    ["T1-018", "Liu & Murphy", 2020, "","","✓","","","","","","","","",""],
    ["T1-019", "Zhang et al.", 2022, "","","✓","","","","✓","","","","",""],
    ["T1-020", "Orsa et al.", 2019, "","","","","","","✓","","","","",""],
    ["T1-021", "Ansari et al.", 2022, "","","","","✓","","","✓","✓","","",""],
    ["T1-022", "Dash et al.", 2022, "","","✓","","","","","","✓","","",""],
    ["T1-023", "Bonfanti & Kohler", 2020, "✓","","","✓","","","","","","","✓","✓"],
    ["T1-024", "Kroll et al.", 2021, "✓","","","✓","","","","","","","✓","✓"],
    ["T1-025", "Kamoun et al.", 2020, "","","","✓","","","","","","","",""],
    ["T1-026", "Adi et al.", 2022, "","","","","","","","","","","","✓"],
    ["T1-027", "Lazic", 2019, "","✓","","","","","","","","✓","",""],
    ["T1-028", "Murugesan", 2022, "","","","","","","","","","✓","",""],
    ["T1-029", "Molloy et al.", 2021, "","","","","","","","","","","",""],
    ["T1-030", "Chan et al.", 2019, "","","","✓","","","","","","","✓",""],
    ["T1-031", "Naik et al.", 2022, "","","","","","","","✓","","","",""],
    ["T1-032", "Li et al.", 2021, "","","","","","","","","","✓","",""],
    ["T1-033", "Truong et al.", 2020, "✓","","","","","","","","","","",""],
    ["T1-034", "Artificial intelligence and machine learning in cybersecurity: applications, challenges, and opportunities for MIS academics", 2022, "✓","✓","✓","✓","✓","✓","✓","✓","✓","✓","✓","✓"],
    ["T1-035", "Artificial intelligence and cybersecurity: Past, presence, and future", 2020, "","✓","✓","✓","","","","✓","","✓","✓","✓"],
    ["T1-036", "Harnessing artificial intelligence capabilities to improve cybersecurity", 2020, "","✓","✓","✓","","","","✓","","","✓",""],
    ["T1-037", "Machine learning cybersecurity adoption in small and medium enterprises in developed countries", 2021, "✓","✓","","","✓","✓","✓","","✓","","✓",""],
    ["T1-038", "Evaluation of AI-based use cases for enhancing the cyber security defense of SMEs", 2022, "","✓","","✓","✓","✓","✓","","✓","","✓",""],
    ["T1-039", "Economics of artificial intelligence in cybersecurity", 2021, "✓","","","","✓","","","","✓","","✓","✓"],
    ["T1-040", "Three ethical challenges of applications of artificial intelligence in cybersecurity", 2019, "","","✓","","","","","","","✓","✓","✓"],
    ["T1-041", "Machine learning techniques applied to cybersecurity", 2019, "","✓","✓","✓","","","","✓","","","✓",""],
    ["T1-042", "AI and Cybersecurity: Opportunities, Challenges, and Governance", 2025, "✓","✓","✓","✓","✓","✓","✓","✓","✓","✓","✓","✓"],
    ["T1-043", "What Hinders Adoption of Artificial Intelligence for Cybersecurity in the Banking Sector (MDPI)", 2024, "✓","✓","✓","✓","✓","✓","✓","✓","✓","✓","✓","✓"],
    ["T1-044", "Adoption of Advanced Cybersecurity Tools by Organizations: Motivations, Barriers, and Leader Responses", 2024, "✓","✓","","✓","✓","✓","✓","","✓","","✓","✓"],
    ["T1-045", "An Iterative Five-Phase Process Model to Successfully Implement AI for Cybersecurity", 2025, "✓","✓","✓","✓","✓","✓","✓","✓","","","",""],
    ["T1-046", "Organizational Adaptation to Generative AI in Cybersecurity: A Systematic Review", 2025, "✓","","✓","","✓","✓","✓","✓","✓","✓","✓","✓"],
    ["T1-047", "Explainable Artificial Intelligence and Cybersecurity: A Systematic Literature Review", 2023, "✓","","✓","✓","","","","","","✓","✓",""],
    ["T1-048", "Security and Privacy for Artificial Intelligence: Opportunities and Challenges", 2021, "","✓","✓","✓","","","","","","✓","✓","✓"],
    ["T1-049", "Responsible AI for Cybersecurity: Assessing the Barriers, Biases and Governance Gaps", 2025, "✓","","✓","✓","✓","✓","✓","✓","✓","✓","✓","✓"],
    ["T1-050", "A Roadmap for SMEs to Adopt an AI Based Cyber Threat Intelligence", 2023, "✓","✓","","✓","✓","✓","✓","✓","✓","","",""],
    ["T1-051", "Generative AI Revolution in Cybersecurity: A Comprehensive Review of Threat Intelligence and Operations", 2025, "✓","✓","✓","✓","","","","✓","","✓","✓","✓"],
    ["T1-052", "Artificial intelligence for cybersecurity: a systematic mapping of literature", 2020, "","✓","✓","✓","","","","✓","","","✓",""],
    ["T1-053", "Adoption of Artificial Intelligence in Cybersecurity for Organizations: Barriers and Roadmap", 2025, "✓","✓","✓","✓","✓","✓","✓","✓","✓","✓","✓","✓"]
]

df = pd.DataFrame(table1_data, columns=cols)

print("\n" + "="*140)
print("COMPONENT 1 — STRUCTURED EXTRACTION TABLE (CONCEPT MATRIX)")
print("="*140 + "\n")
print(df.to_markdown(index=False))

bin_df = df[barriers].map(lambda x: 1 if x == "✓" else 0)

print("\nSummary:")
print(f"- Total Papers Processed: {len(df)}")
print(f"- Total Barriers Evaluated: {len(barriers)}")
print(f"- Avg Barrier Coverage per Paper: {bin_df.sum(axis=1).mean():.2f}")

print("\n" + "="*140)
print("COMPONENT 2 — BARRIER PRIORITIZATION & READINESS RANKING")
print("="*140 + "\n")

barrier_freq = bin_df.sum()
weights = 1 / (barrier_freq + 1)
weights /= weights.sum()

df["Barrier_Count"] = bin_df.sum(axis=1)
df["Weighted_Score"] = (bin_df * weights).sum(axis=1)
df["Rank"] = df["Weighted_Score"].rank(ascending=False, method="min").astype(int)
df_sorted = df.sort_values("Rank")

print("### Weighted Barrier Prioritization (Least-Covered = Highest Priority)\n")
print(weights.sort_values(ascending=False).round(4).to_markdown())

print("\n### Top Papers by Weighted Readiness Score\n")
columns = ["Rank","Paper_Name","Year","Paper_ID","Weighted_Score","Barrier_Count"]
print(df_sorted[columns].round(4).to_markdown(index=False))

print("\n### Strategic Research Gap Insights\n")
rare = weights.sort_values(ascending=False).head(5).index.tolist()
print("Top 5 Most Under-represented Barriers:")
for i, barrier in enumerate(rare, start=1):
    print(f"{i}. {barrier}")
