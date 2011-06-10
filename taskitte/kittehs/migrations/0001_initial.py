# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'List'
        db.create_table('kittehs_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='30')),
        ))
        db.send_create_signal('kittehs', ['List'])

        # Adding model 'Task'
        db.create_table('kittehs_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kittehs.List'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='50')),
            ('description', self.gf('django.db.models.fields.TextField')(max_length='280', null=True, blank=True)),
            ('even_more_info', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('is_claimed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email_list', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['kittehs.TinyMailingList'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('kittehs', ['Task'])

        # Adding M2M table for field claimants on 'Task'
        db.create_table('kittehs_task_claimants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm['kittehs.task'], null=False)),
            ('person', models.ForeignKey(orm['kittehs.person'], null=False))
        ))
        db.create_unique('kittehs_task_claimants', ['task_id', 'person_id'])

        # Adding model 'Person'
        db.create_table('kittehs_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('kittehs', ['Person'])

        # Adding model 'TinyMailingList'
        db.create_table('kittehs_tinymailinglist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='30')),
        ))
        db.send_create_signal('kittehs', ['TinyMailingList'])

        # Adding M2M table for field members on 'TinyMailingList'
        db.create_table('kittehs_tinymailinglist_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tinymailinglist', models.ForeignKey(orm['kittehs.tinymailinglist'], null=False)),
            ('person', models.ForeignKey(orm['kittehs.person'], null=False))
        ))
        db.create_unique('kittehs_tinymailinglist_members', ['tinymailinglist_id', 'person_id'])


    def backwards(self, orm):
        
        # Deleting model 'List'
        db.delete_table('kittehs_list')

        # Deleting model 'Task'
        db.delete_table('kittehs_task')

        # Removing M2M table for field claimants on 'Task'
        db.delete_table('kittehs_task_claimants')

        # Deleting model 'Person'
        db.delete_table('kittehs_person')

        # Deleting model 'TinyMailingList'
        db.delete_table('kittehs_tinymailinglist')

        # Removing M2M table for field members on 'TinyMailingList'
        db.delete_table('kittehs_tinymailinglist_members')


    models = {
        'kittehs.list': {
            'Meta': {'object_name': 'List'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'30'"})
        },
        'kittehs.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'30'"})
        },
        'kittehs.task': {
            'Meta': {'object_name': 'Task'},
            'claimants': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['kittehs.Person']", 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': "'280'", 'null': 'True', 'blank': 'True'}),
            'email_list': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['kittehs.TinyMailingList']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'even_more_info': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_claimed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kittehs.List']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'50'"})
        },
        'kittehs.tinymailinglist': {
            'Meta': {'object_name': 'TinyMailingList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['kittehs.Person']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'30'"})
        }
    }

    complete_apps = ['kittehs']
