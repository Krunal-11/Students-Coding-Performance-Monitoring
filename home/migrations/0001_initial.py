# Generated by Django 5.0 on 2024-01-02 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentScores',
            fields=[
                ('roll_no', models.CharField(db_column='ROLL_NO', max_length=10, primary_key=True, serialize=False)),
                ('hackerrank', models.TextField(blank=True, db_column='HackerRank', null=True)),
                ('hackerrank_score', models.IntegerField(db_column='HackerRank_Score')),
                ('codeforces', models.TextField(blank=True, db_column='CodeForces', null=True)),
                ('codeforces_score', models.IntegerField(db_column='CodeForces_Score')),
                ('codechef', models.TextField(blank=True, db_column='CodeChef', null=True)),
                ('codechef_score', models.IntegerField(db_column='CodeChef_Score')),
                ('spoj', models.TextField(blank=True, db_column='Spoj', null=True)),
                ('spoj_score', models.IntegerField(db_column='Spoj_Score')),
                ('interviewbit', models.TextField(blank=True, db_column='InterviewBit', null=True)),
                ('interviewbit_score', models.IntegerField(db_column='InterviewBit_Score')),
                ('leetcode', models.TextField(blank=True, db_column='LeetCode', null=True)),
                ('leetcode_score', models.IntegerField(db_column='LeetCode_Score')),
                ('gfg', models.TextField(blank=True, db_column='GFG', null=True)),
                ('gfg_score', models.IntegerField(db_column='GFG_Score')),
                ('overall_score', models.IntegerField(db_column='Overall_score')),
                ('daily_scores', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'student_scores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentMaster',
            fields=[
                ('rank', models.IntegerField(blank=True, db_column='RANK', null=True)),
                ('roll_no', models.OneToOneField(db_column='ROLL_NO', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='home.studentscores')),
                ('name', models.CharField(db_column='NAME', max_length=39)),
                ('course', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Course', max_length=7, null=True)),
                ('year', models.IntegerField(blank=True, db_column='Year', null=True)),
                ('branch', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Branch', max_length=3, null=True)),
                ('sec', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Sec', max_length=1, null=True)),
                ('hackerrank_username', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='HackerRank_Username', max_length=48, null=True)),
                ('codeforces_username', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='CodeForces_Username', max_length=40, null=True)),
                ('codechef_username', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='CodeChef_Username', max_length=92, null=True)),
                ('spoj_username', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Spoj_Username', max_length=22, null=True)),
                ('interviewbit_username', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='InterviewBit_Username', max_length=42, null=True)),
                ('leetcode_username', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='LeetCode_Username', max_length=29, null=True)),
                ('gfg_username', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='GFG_Username', max_length=48, null=True)),
            ],
            options={
                'db_table': 'student_master',
                'managed': False,
            },
        ),
    ]
