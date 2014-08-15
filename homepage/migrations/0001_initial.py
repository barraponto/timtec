# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomePage'
        db.create_table(u'homepage_homepage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('greeting_background', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('greeting_message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('greeting_button', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('promoted_courses_lead', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('promoted_courses_message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('promoted_courses_button', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('promoted_menthors_lead', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('promoted_menthors_message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('promoted_menthors_button', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('promoted_portfolios_lead', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('promoted_portfolios_message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('promoted_portfolios_button', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('brand_logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('brand_lead', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('brand_message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('brand_button', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
        ))
        db.send_create_signal(u'homepage', ['HomePage'])

        # Adding model 'HomePageCourse'
        db.create_table(u'homepage_homepagecourse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['homepage.HomePage'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Course'])),
        ))
        db.send_create_signal(u'homepage', ['HomePageCourse'])

        # Adding unique constraint on 'HomePageCourse', fields ['homepage', 'course']
        db.create_unique(u'homepage_homepagecourse', ['homepage_id', 'course_id'])

        # Adding model 'HomePageMenthor'
        db.create_table(u'homepage_homepagementhor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['homepage.HomePage'])),
            ('menthor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.TimtecUser'])),
        ))
        db.send_create_signal(u'homepage', ['HomePageMenthor'])

        # Adding unique constraint on 'HomePageMenthor', fields ['homepage', 'menthor']
        db.create_unique(u'homepage_homepagementhor', ['homepage_id', 'menthor_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'HomePageMenthor', fields ['homepage', 'menthor']
        db.delete_unique(u'homepage_homepagementhor', ['homepage_id', 'menthor_id'])

        # Removing unique constraint on 'HomePageCourse', fields ['homepage', 'course']
        db.delete_unique(u'homepage_homepagecourse', ['homepage_id', 'course_id'])

        # Deleting model 'HomePage'
        db.delete_table(u'homepage_homepage')

        # Deleting model 'HomePageCourse'
        db.delete_table(u'homepage_homepagecourse')

        # Deleting model 'HomePageMenthor'
        db.delete_table(u'homepage_homepagementhor')


    models = {
        u'accounts.timtecuser': {
            'Meta': {'object_name': 'TimtecUser'},
            'accepted_terms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.course': {
            'Meta': {'object_name': 'Course'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'application': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'home_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'home_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'home_thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Video']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'professors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'professorcourse_set'", 'symmetrical': 'False', 'through': u"orm['core.CourseProfessor']", 'to': u"orm['accounts.TimtecUser']"}),
            'pronatec': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'publication': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'requirement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '64'}),
            'structure': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'studentcourse_set'", 'symmetrical': 'False', 'through': u"orm['core.CourseStudent']", 'to': u"orm['accounts.TimtecUser']"}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'workload': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'core.courseprofessor': {
            'Meta': {'unique_together': "(('user', 'course'),)", 'object_name': 'CourseProfessor'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "'instructor'", 'max_length': '128'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.TimtecUser']"})
        },
        u'core.coursestudent': {
            'Meta': {'unique_together': "(('user', 'course'),)", 'object_name': 'CourseStudent'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.TimtecUser']"})
        },
        u'core.video': {
            'Meta': {'object_name': 'Video'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'homepage.homepage': {
            'Meta': {'object_name': 'HomePage'},
            'brand_button': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'brand_lead': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'brand_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'brand_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'greeting_background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'greeting_button': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'greeting_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promoted_courses': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'+'", 'blank': 'True', 'through': u"orm['homepage.HomePageCourse']", 'to': u"orm['core.Course']"}),
            'promoted_courses_button': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'promoted_courses_lead': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'promoted_courses_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'promoted_menthors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'+'", 'blank': 'True', 'through': u"orm['homepage.HomePageMenthor']", 'to': u"orm['accounts.TimtecUser']"}),
            'promoted_menthors_button': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'promoted_menthors_lead': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'promoted_menthors_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'promoted_portfolios_button': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'promoted_portfolios_lead': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'promoted_portfolios_message': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'homepage.homepagecourse': {
            'Meta': {'unique_together': "(('homepage', 'course'),)", 'object_name': 'HomePageCourse'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Course']"}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['homepage.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'homepage.homepagementhor': {
            'Meta': {'unique_together': "(('homepage', 'menthor'),)", 'object_name': 'HomePageMenthor'},
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['homepage.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menthor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.TimtecUser']"})
        }
    }

    complete_apps = ['homepage']