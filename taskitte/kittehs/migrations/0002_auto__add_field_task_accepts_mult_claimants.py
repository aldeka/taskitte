# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Task.accepts_mult_claimants'
        db.add_column('kittehs_task', 'accepts_mult_claimants', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Task.accepts_mult_claimants'
        db.delete_column('kittehs_task', 'accepts_mult_claimants')


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
            'accepts_mult_claimants': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
