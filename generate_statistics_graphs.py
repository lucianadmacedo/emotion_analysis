#!/usr/bin/env python3
"""
Generate statistical visualization graphs from subreddit emotion analysis
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Set style
plt.style.use('dark_background')

# Load data
output_dir = Path("/Users/lucianadiasdemacedo/Downloads/corpus_expansion/emotion_analysis")

with open(output_dir / 'internationalstudents_analysis.json', 'r') as f:
    intl_data = json.load(f)

with open(output_dir / 'college_analysis.json', 'r') as f:
    college_data = json.load(f)

# Prepare data
intl_emotions = intl_data['emotions']
college_emotions = college_data['emotions']

# All emotion categories
all_emotions = sorted(set(list(intl_emotions.keys()) + list(college_emotions.keys())))

# 1. Side-by-side bar chart comparing emotions
fig, ax = plt.subplots(figsize=(14, 8))
x = np.arange(len(all_emotions))
width = 0.35

intl_counts = [intl_emotions.get(e, 0) for e in all_emotions]
college_counts = [college_emotions.get(e, 0) for e in all_emotions]

bars1 = ax.bar(x - width/2, intl_counts, width, label='r/InternationalStudents', color='#FF6B6B', alpha=0.8)
bars2 = ax.bar(x + width/2, college_counts, width, label='r/college', color='#4ECDC4', alpha=0.8)

ax.set_xlabel('Emotions', fontsize=14, fontweight='bold')
ax.set_ylabel('Count', fontsize=14, fontweight='bold')
ax.set_title('Emotion Distribution Comparison\nr/InternationalStudents vs r/college', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels([e.capitalize() for e in all_emotions], rotation=45, ha='right')
ax.legend(fontsize=12)
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig(output_dir / 'emotion_comparison_bar.png', dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✓ Saved: emotion_comparison_bar.png")
plt.close()

# 2. Pie charts for each subreddit
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# International Students pie
colors_intl = plt.cm.Set3(np.linspace(0, 1, len(intl_emotions)))
wedges1, texts1, autotexts1 = ax1.pie(
    intl_emotions.values(),
    labels=[e.capitalize() for e in intl_emotions.keys()],
    autopct='%1.1f%%',
    colors=colors_intl,
    startangle=90,
    textprops={'fontsize': 11}
)
ax1.set_title(f'r/InternationalStudents\nEmotion Distribution\n({intl_data["posts_analyzed"]} posts)',
              fontsize=14, fontweight='bold', pad=15)

# College pie
colors_college = plt.cm.Set2(np.linspace(0, 1, len(college_emotions)))
wedges2, texts2, autotexts2 = ax2.pie(
    college_emotions.values(),
    labels=[e.capitalize() for e in college_emotions.keys()],
    autopct='%1.1f%%',
    colors=colors_college,
    startangle=90,
    textprops={'fontsize': 11}
)
ax2.set_title(f'r/college\nEmotion Distribution\n({college_data["posts_analyzed"]} posts)',
              fontsize=14, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig(output_dir / 'emotion_pie_charts.png', dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✓ Saved: emotion_pie_charts.png")
plt.close()

# 3. Percentage comparison (normalized)
fig, ax = plt.subplots(figsize=(14, 8))

intl_total = sum(intl_emotions.values())
college_total = sum(college_emotions.values())

intl_pct = [(intl_emotions.get(e, 0) / intl_total * 100) for e in all_emotions]
college_pct = [(college_emotions.get(e, 0) / college_total * 100) for e in all_emotions]

x = np.arange(len(all_emotions))
width = 0.35

bars1 = ax.bar(x - width/2, intl_pct, width, label='r/InternationalStudents', color='#FF6B6B', alpha=0.8)
bars2 = ax.bar(x + width/2, college_pct, width, label='r/college', color='#4ECDC4', alpha=0.8)

ax.set_xlabel('Emotions', fontsize=14, fontweight='bold')
ax.set_ylabel('Percentage (%)', fontsize=14, fontweight='bold')
ax.set_title('Emotion Distribution (Normalized Percentages)\nr/InternationalStudents vs r/college',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels([e.capitalize() for e in all_emotions], rotation=45, ha='right')
ax.legend(fontsize=12)
ax.grid(axis='y', alpha=0.3)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%',
                   ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig(output_dir / 'emotion_percentage_comparison.png', dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✓ Saved: emotion_percentage_comparison.png")
plt.close()

# 4. Top entities bar chart for International Students
fig, ax = plt.subplots(figsize=(14, 8))

intl_entities = intl_data['entities']
top_intl_entities = sorted(intl_entities.items(), key=lambda x: x[1], reverse=True)[:20]
entities_names = [e[0] for e in top_intl_entities]
entities_counts = [e[1] for e in top_intl_entities]

bars = ax.barh(entities_names, entities_counts, color='#FF6B6B', alpha=0.8)
ax.set_xlabel('Mention Count', fontsize=14, fontweight='bold')
ax.set_ylabel('Entity', fontsize=14, fontweight='bold')
ax.set_title('Top 20 Entities - r/InternationalStudents', fontsize=16, fontweight='bold', pad=15)
ax.invert_yaxis()
ax.grid(axis='x', alpha=0.3)

# Add value labels
for i, (bar, count) in enumerate(zip(bars, entities_counts)):
    ax.text(count, i, f' {count}', va='center', fontsize=10)

plt.tight_layout()
plt.savefig(output_dir / 'top_entities_internationalstudents.png', dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✓ Saved: top_entities_internationalstudents.png")
plt.close()

# 5. Top entities bar chart for College
fig, ax = plt.subplots(figsize=(14, 8))

college_entities = college_data['entities']
top_college_entities = sorted(college_entities.items(), key=lambda x: x[1], reverse=True)[:20]
entities_names = [e[0] for e in top_college_entities]
entities_counts = [e[1] for e in top_college_entities]

bars = ax.barh(entities_names, entities_counts, color='#4ECDC4', alpha=0.8)
ax.set_xlabel('Mention Count', fontsize=14, fontweight='bold')
ax.set_ylabel('Entity', fontsize=14, fontweight='bold')
ax.set_title('Top 20 Entities - r/college', fontsize=16, fontweight='bold', pad=15)
ax.invert_yaxis()
ax.grid(axis='x', alpha=0.3)

# Add value labels
for i, (bar, count) in enumerate(zip(bars, entities_counts)):
    ax.text(count, i, f' {count}', va='center', fontsize=10)

plt.tight_layout()
plt.savefig(output_dir / 'top_entities_college.png', dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✓ Saved: top_entities_college.png")
plt.close()

# 6. Emotion heatmap showing intensity
fig, ax = plt.subplots(figsize=(12, 6))

emotions_list = sorted(all_emotions)
subreddits = ['r/InternationalStudents', 'r/college']

# Create matrix
data_matrix = []
for subreddit in subreddits:
    if subreddit == 'r/InternationalStudents':
        total = sum(intl_emotions.values())
        row = [(intl_emotions.get(e, 0) / total * 100) for e in emotions_list]
    else:
        total = sum(college_emotions.values())
        row = [(college_emotions.get(e, 0) / total * 100) for e in emotions_list]
    data_matrix.append(row)

im = ax.imshow(data_matrix, cmap='YlOrRd', aspect='auto')

# Set ticks
ax.set_xticks(np.arange(len(emotions_list)))
ax.set_yticks(np.arange(len(subreddits)))
ax.set_xticklabels([e.capitalize() for e in emotions_list], rotation=45, ha='right')
ax.set_yticklabels(subreddits, fontsize=12)

# Add colorbar
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Percentage (%)', rotation=270, labelpad=20, fontsize=12)

# Add text annotations
for i in range(len(subreddits)):
    for j in range(len(emotions_list)):
        text = ax.text(j, i, f'{data_matrix[i][j]:.1f}%',
                      ha="center", va="center", color="white" if data_matrix[i][j] > 10 else "black",
                      fontsize=10, fontweight='bold')

ax.set_title('Emotion Distribution Heatmap', fontsize=16, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(output_dir / 'emotion_heatmap.png', dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✓ Saved: emotion_heatmap.png")
plt.close()

# 7. Scraping metadata pie chart
fig, ax = plt.subplots(figsize=(10, 8))

subreddit_counts = {
    'r/InternationalStudents': 49,
    'r/college': 61,
    'r/StudentLoans': 50,
    'r/financialaid': 50,
    'r/Harvard': 50
}

colors = ['#FF6B6B', '#4ECDC4', '#95E1D3', '#F38181', '#AA96DA']
wedges, texts, autotexts = ax.pie(
    subreddit_counts.values(),
    labels=subreddit_counts.keys(),
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    textprops={'fontsize': 12, 'fontweight': 'bold'}
)

ax.set_title('Reddit Scraping Distribution\nTotal: 249 posts', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig(output_dir / 'scraping_distribution.png', dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✓ Saved: scraping_distribution.png")
plt.close()

print("\n" + "="*60)
print("✓ All graphs generated successfully!")
print("="*60)
print(f"\nGraphs saved to: {output_dir}")
print("\nGenerated files:")
print("  1. emotion_comparison_bar.png")
print("  2. emotion_pie_charts.png")
print("  3. emotion_percentage_comparison.png")
print("  4. top_entities_internationalstudents.png")
print("  5. top_entities_college.png")
print("  6. emotion_heatmap.png")
print("  7. scraping_distribution.png")
