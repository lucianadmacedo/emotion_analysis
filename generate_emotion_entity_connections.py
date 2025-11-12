#!/usr/bin/env python3
"""
Generate visualizations showing top 2 entities connected to each emotion
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

# Get emotion-entity connections
intl_connections = intl_data['emotion_entity_connections']
college_connections = college_data['emotion_entity_connections']

# Get top 2 entities for each emotion
def get_top_entities_per_emotion(connections, n=2):
    result = {}
    for emotion, entities in connections.items():
        top_entities = sorted(entities.items(), key=lambda x: x[1], reverse=True)[:n]
        result[emotion] = top_entities
    return result

intl_top = get_top_entities_per_emotion(intl_connections, 2)
college_top = get_top_entities_per_emotion(college_connections, 2)

# Sort emotions by total count
intl_emotion_totals = intl_data['emotions']
college_emotion_totals = college_data['emotions']

sorted_intl_emotions = sorted(intl_emotion_totals.items(), key=lambda x: x[1], reverse=True)
sorted_college_emotions = sorted(college_emotion_totals.items(), key=lambda x: x[1], reverse=True)

# 1. International Students - Top 2 entities per emotion
fig, ax = plt.subplots(figsize=(14, 10))

emotions = [e[0] for e in sorted_intl_emotions]
y_pos = np.arange(len(emotions)) * 3  # Space out emotions

colors = ['#FF6B6B', '#FF8E8E']  # Two shades of red/pink

for i, emotion in enumerate(emotions):
    if emotion in intl_top:
        top_entities = intl_top[emotion]

        # Draw bars for top 2 entities
        for j, (entity, count) in enumerate(top_entities):
            bar_pos = y_pos[i] + j * 0.8
            bar = ax.barh(bar_pos, count, height=0.7, color=colors[j], alpha=0.9)

            # Add entity name and count
            entity_display = entity if len(entity) <= 30 else entity[:27] + '...'
            ax.text(count + 2, bar_pos, f'{entity_display} ({count})',
                   va='center', fontsize=11, fontweight='bold')

        # Add emotion label on the left
        ax.text(-5, y_pos[i] + 0.4, emotion.upper(),
               va='center', ha='right', fontsize=12, fontweight='bold',
               color='#FFD700')

ax.set_xlabel('Connection Count', fontsize=14, fontweight='bold')
ax.set_title('r/InternationalStudents: Top 2 Entities per Emotion',
             fontsize=16, fontweight='bold', pad=20)
ax.set_yticks([])
ax.grid(axis='x', alpha=0.3)
ax.set_xlim(-10, max([max([e[1] for e in entities]) for entities in intl_top.values()]) * 1.2)

# Add legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=colors[0], label='Top Entity'),
    Patch(facecolor=colors[1], label='2nd Entity')
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=11)

plt.tight_layout()
plt.savefig(output_dir / 'emotion_top2_entities_internationalstudents.png',
           dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✓ Saved: emotion_top2_entities_internationalstudents.png")
plt.close()

# 2. College - Top 2 entities per emotion
fig, ax = plt.subplots(figsize=(14, 10))

emotions = [e[0] for e in sorted_college_emotions]
y_pos = np.arange(len(emotions)) * 3

colors = ['#4ECDC4', '#7DDFD9']  # Two shades of teal

for i, emotion in enumerate(emotions):
    if emotion in college_top:
        top_entities = college_top[emotion]

        # Draw bars for top 2 entities
        for j, (entity, count) in enumerate(top_entities):
            bar_pos = y_pos[i] + j * 0.8
            bar = ax.barh(bar_pos, count, height=0.7, color=colors[j], alpha=0.9)

            # Add entity name and count
            entity_display = entity if len(entity) <= 30 else entity[:27] + '...'
            ax.text(count + 2, bar_pos, f'{entity_display} ({count})',
                   va='center', fontsize=11, fontweight='bold')

        # Add emotion label on the left
        ax.text(-5, y_pos[i] + 0.4, emotion.upper(),
               va='center', ha='right', fontsize=12, fontweight='bold',
               color='#FFD700')

ax.set_xlabel('Connection Count', fontsize=14, fontweight='bold')
ax.set_title('r/college: Top 2 Entities per Emotion',
             fontsize=16, fontweight='bold', pad=20)
ax.set_yticks([])
ax.grid(axis='x', alpha=0.3)
ax.set_xlim(-10, max([max([e[1] for e in entities]) for entities in college_top.values()]) * 1.2)

# Add legend
legend_elements = [
    Patch(facecolor=colors[0], label='Top Entity'),
    Patch(facecolor=colors[1], label='2nd Entity')
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=11)

plt.tight_layout()
plt.savefig(output_dir / 'emotion_top2_entities_college.png',
           dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✓ Saved: emotion_top2_entities_college.png")
plt.close()

# 3. Side-by-side comparison for major emotions
major_emotions = ['anxiety', 'hope', 'fear', 'sadness', 'joy', 'relief']
existing_major = [e for e in major_emotions if e in intl_top or e in college_top]

fig, axes = plt.subplots(len(existing_major), 2, figsize=(18, 4*len(existing_major)))

if len(existing_major) == 1:
    axes = [axes]

for idx, emotion in enumerate(existing_major):
    # International Students (left)
    ax_intl = axes[idx][0]
    if emotion in intl_top:
        entities = intl_top[emotion]
        entity_names = [e[0] if len(e[0]) <= 25 else e[0][:22]+'...' for e in entities]
        entity_counts = [e[1] for e in entities]

        bars = ax_intl.barh(range(len(entities)), entity_counts, color='#FF6B6B', alpha=0.9)
        ax_intl.set_yticks(range(len(entities)))
        ax_intl.set_yticklabels(entity_names, fontsize=12)
        ax_intl.invert_yaxis()

        # Add value labels
        for i, (bar, count) in enumerate(zip(bars, entity_counts)):
            ax_intl.text(count + 1, i, f'{count}', va='center', fontsize=11, fontweight='bold')

        ax_intl.set_xlabel('Connections', fontsize=11, fontweight='bold')
        ax_intl.set_title(f'{emotion.upper()}\nr/InternationalStudents',
                         fontsize=13, fontweight='bold', pad=10)
        ax_intl.grid(axis='x', alpha=0.3)
    else:
        ax_intl.text(0.5, 0.5, 'No data', ha='center', va='center', fontsize=12)
        ax_intl.set_title(f'{emotion.upper()}\nr/InternationalStudents',
                         fontsize=13, fontweight='bold', pad=10)
        ax_intl.axis('off')

    # College (right)
    ax_college = axes[idx][1]
    if emotion in college_top:
        entities = college_top[emotion]
        entity_names = [e[0] if len(e[0]) <= 25 else e[0][:22]+'...' for e in entities]
        entity_counts = [e[1] for e in entities]

        bars = ax_college.barh(range(len(entities)), entity_counts, color='#4ECDC4', alpha=0.9)
        ax_college.set_yticks(range(len(entities)))
        ax_college.set_yticklabels(entity_names, fontsize=12)
        ax_college.invert_yaxis()

        # Add value labels
        for i, (bar, count) in enumerate(zip(bars, entity_counts)):
            ax_college.text(count + 1, i, f'{count}', va='center', fontsize=11, fontweight='bold')

        ax_college.set_xlabel('Connections', fontsize=11, fontweight='bold')
        ax_college.set_title(f'{emotion.upper()}\nr/college',
                           fontsize=13, fontweight='bold', pad=10)
        ax_college.grid(axis='x', alpha=0.3)
    else:
        ax_college.text(0.5, 0.5, 'No data', ha='center', va='center', fontsize=12)
        ax_college.set_title(f'{emotion.upper()}\nr/college',
                           fontsize=13, fontweight='bold', pad=10)
        ax_college.axis('off')

plt.suptitle('Top 2 Entities per Major Emotion - Comparison',
            fontsize=18, fontweight='bold', y=1.001)
plt.tight_layout()
plt.savefig(output_dir / 'emotion_top2_comparison.png',
           dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✓ Saved: emotion_top2_comparison.png")
plt.close()

# 4. Create a detailed table-style visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 12))

# International Students table
ax1.axis('tight')
ax1.axis('off')

intl_table_data = []
for emotion in sorted_intl_emotions:
    emotion_name = emotion[0]
    emotion_count = emotion[1]
    if emotion_name in intl_top:
        entities = intl_top[emotion_name]
        if len(entities) >= 2:
            intl_table_data.append([
                f"{emotion_name.upper()}\n({emotion_count})",
                f"{entities[0][0]}\n({entities[0][1]})",
                f"{entities[1][0]}\n({entities[1][1]})"
            ])
        elif len(entities) == 1:
            intl_table_data.append([
                f"{emotion_name.upper()}\n({emotion_count})",
                f"{entities[0][0]}\n({entities[0][1]})",
                "-"
            ])

table1 = ax1.table(cellText=intl_table_data,
                   colLabels=['Emotion\n(count)', 'Top Entity\n(connections)', '2nd Entity\n(connections)'],
                   cellLoc='left',
                   loc='center',
                   colWidths=[0.25, 0.4, 0.4])

table1.auto_set_font_size(False)
table1.set_fontsize(11)
table1.scale(1, 3)

# Style header
for i in range(3):
    table1[(0, i)].set_facecolor('#FF6B6B')
    table1[(0, i)].set_text_props(weight='bold', fontsize=12)

# Style cells
for i in range(1, len(intl_table_data) + 1):
    table1[(i, 0)].set_facecolor('#2a2a2a')
    table1[(i, 1)].set_facecolor('#1e1e1e')
    table1[(i, 2)].set_facecolor('#1e1e1e')
    table1[(i, 0)].set_text_props(weight='bold', color='#FFD700')

ax1.set_title('r/InternationalStudents\nEmotion → Entity Connections',
             fontsize=16, fontweight='bold', pad=20)

# College table
ax2.axis('tight')
ax2.axis('off')

college_table_data = []
for emotion in sorted_college_emotions:
    emotion_name = emotion[0]
    emotion_count = emotion[1]
    if emotion_name in college_top:
        entities = college_top[emotion_name]
        if len(entities) >= 2:
            college_table_data.append([
                f"{emotion_name.upper()}\n({emotion_count})",
                f"{entities[0][0]}\n({entities[0][1]})",
                f"{entities[1][0]}\n({entities[1][1]})"
            ])
        elif len(entities) == 1:
            college_table_data.append([
                f"{emotion_name.upper()}\n({emotion_count})",
                f"{entities[0][0]}\n({entities[0][1]})",
                "-"
            ])

table2 = ax2.table(cellText=college_table_data,
                   colLabels=['Emotion\n(count)', 'Top Entity\n(connections)', '2nd Entity\n(connections)'],
                   cellLoc='left',
                   loc='center',
                   colWidths=[0.25, 0.4, 0.4])

table2.auto_set_font_size(False)
table2.set_fontsize(11)
table2.scale(1, 3)

# Style header
for i in range(3):
    table2[(0, i)].set_facecolor('#4ECDC4')
    table2[(0, i)].set_text_props(weight='bold', fontsize=12)

# Style cells
for i in range(1, len(college_table_data) + 1):
    table2[(i, 0)].set_facecolor('#2a2a2a')
    table2[(i, 1)].set_facecolor('#1e1e1e')
    table2[(i, 2)].set_facecolor('#1e1e1e')
    table2[(i, 0)].set_text_props(weight='bold', color='#FFD700')

ax2.set_title('r/college\nEmotion → Entity Connections',
             fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig(output_dir / 'emotion_entity_table.png',
           dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✓ Saved: emotion_entity_table.png")
plt.close()

print("\n" + "="*60)
print("✓ All emotion-entity connection graphs generated!")
print("="*60)
print(f"\nGraphs saved to: {output_dir}")
print("\nGenerated files:")
print("  1. emotion_top2_entities_internationalstudents.png")
print("  2. emotion_top2_entities_college.png")
print("  3. emotion_top2_comparison.png")
print("  4. emotion_entity_table.png")
