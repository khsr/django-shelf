# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'TwitterProfile.last_post_time'
        db.add_column('social_discovery_twitterprofile', 'last_post_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'TwitterProfile.last_post_time'
        db.delete_column('social_discovery_twitterprofile', 'last_post_time')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 3, 19, 10, 12, 32, 314188)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 3, 19, 10, 12, 32, 314026)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'debra.demographicslocality': {
            'Meta': {'object_name': 'DemographicsLocality'},
            'city': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        'debra.influencer': {
            'Meta': {'object_name': 'Influencer'},
            'about_url': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'accuracy_validated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'activity_level': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'autodetected_attributes': ('django_pgjson.fields.JsonField', [], {}),
            'autoverified_fields': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'average_num_comments_per_giveaway': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'average_num_comments_per_post': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'average_num_comments_per_sponsored_post': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'average_num_giveaways': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'average_num_posts': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'blacklist_reasons': ('djorm_pgarray.fields.TextArrayField', [], {'default': 'None', u'dbtype': "u'text'", 'blank': 'True'}),
            'blacklisted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blog_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'blogger_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'bloglovin_followers': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'bloglovin_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'blogname': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'categories': ('django_pgjson.fields.JsonField', [], {}),
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'collaboration_types': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'contact_form_if_no_email': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'copyrightable_content': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_upgraded_to_show_on_search': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_validated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'demographics_bloggerage': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'demographics_gender': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'demographics_locality': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'influencers'", 'null': 'True', 'to': "orm['debra.DemographicsLocality']"}),
            'demographics_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'demographics_location_lat': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'demographics_location_lon': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'demographics_location_normalized': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'email_all_other': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'email_for_advertising_or_collaborations': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'fb_blogger_mistake': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fb_couldnt_find': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fb_crawler_problem': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fb_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'gplus_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'how_you_work': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_blogger_mistake': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'in_couldnt_find': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'in_crawler_problem': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'insta_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'is_live': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'latest_in_influencer_score': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'lb_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'old_show_on_search': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'pin_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'pn_blogger_mistake': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pn_couldnt_find': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pn_crawler_problem': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pose_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'posts_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'price_range_tag_normalized': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'problem': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'profile_pic_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'qa': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'ready_to_invite': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'relevant_to_fashion': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'remove_tag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'score_engagement_overall': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'score_popularity_overall': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'shelf_user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'show_on_search': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'tw_blogger_mistake': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tw_couldnt_find': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tw_crawler_problem': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tw_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'validated_on': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'youtube_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        'debra.platform': {
            'Meta': {'unique_together': "(('platform_name', 'validated_handle', 'influencer'),)", 'object_name': 'Platform'},
            'about': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'activity_level': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'api_calls': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'autovalidated': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'autovalidated_reason': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'avg_numcomments_non_sponsored': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avg_numcomments_overall': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avg_numcomments_sponsored': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avg_numlikes_non_sponsored': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avg_numlikes_overall': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avg_numlikes_sponsored': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avg_numshares_non_sponsored': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avg_numshares_overall': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avg_numshares_sponsored': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'blogname': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'content_lang': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'cover_img_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'detected_demographics_gender': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'detected_demographics_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'detected_influencer_attributes': ('django_pgjson.fields.JsonField', [], {}),
            'detected_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'feed_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'feed_url_last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'fetcher_class': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indepth_processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'influencer': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['debra.Influencer']", 'null': 'True', 'blank': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'last_api_call': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'last_fetched': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'num_followers': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'num_following': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'numposts': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'numsponsoredposts': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'only_summary_from_feed': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'platform_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'platform_state': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'posting_rate': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'processing_state': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'profile_img_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'score_engagement_non_sponsored': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'score_engagement_overall': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'score_engagement_sponsored': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'score_popularity_overall': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'total_numcomments': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'total_numlikes': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'total_numshares': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'url_not_found': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'validated': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'validated_handle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1000', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'social_discovery.twitterfollow': {
            'Meta': {'object_name': 'TwitterFollow'},
            'followed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'followed'", 'to': "orm['social_discovery.TwitterProfile']"}),
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'folowers'", 'to': "orm['social_discovery.TwitterProfile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'social_discovery.twitterprofile': {
            'Meta': {'object_name': 'TwitterProfile'},
            'discovered_influencer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'twitter_profile'", 'null': 'True', 'to': "orm['debra.Influencer']"}),
            'followers_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'friends+'", 'symmetrical': 'False', 'through': "orm['social_discovery.TwitterFollow']", 'to': "orm['social_discovery.TwitterProfile']"}),
            'friends_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'friends_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_post_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'platform': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'twitter_profile'", 'null': 'True', 'to': "orm['debra.Platform']"}),
            'post_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profile_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'screen_name': ('django.db.models.fields.TextField', [], {'unique': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['social_discovery']
