<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="{$CurrentLocale}">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="globalsign-domain-verification" content="tWFOHNAA_WMHmHfBMq38uTgupHFugV_dZ2rqyRxNMx" />
    <title>$Title - OpenStack is open source software for creating private and public clouds.</title>

    $MetaTags(false)

    <% base_tag %>

    <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="http://www.openstack.org/blog/feed/" />


    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
    <script src="//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="//oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
    <% include Page_GoogleAnalytics %>

</head>

<body id="$URLSegment">
    <% include SiteBanner %>
    <% include Navigation %>
<!-- Page Content -->
    $Message
<div id="language-selector"></div>
    $Layout
    <% include Footer %>
    <% include Quantcast %>
    <% include TwitterUniversalWebsiteTagCode %>
    <% include GoogleAdWordsSnippet %>
</body>
    <% include Page_LinkedinInsightTracker %>
    $ModuleJS('paper-page')
    $ModuleCSS('paper-page')
</html>