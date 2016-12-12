/**
 * @license Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	config.uiColor = '#333';
	config.textColor = '#fff';
	config.removePlugins = 'elementspath';
	config.disableNativeSpellChecker = false;
	config.allowedContent = true;
	config.resize_enabled = false;
	config.skin = 'bootstrapck';
	config.extraPlugins = 'autogrow, SimpleLink, SimpleImage, smiley';
};
