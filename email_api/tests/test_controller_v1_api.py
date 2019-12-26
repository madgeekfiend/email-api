import os
import pytest

from email_api import app

RAW_EMAIL_MESSAGE = """```Return-Path: <infos@contact-darty.com>
X-Original-To: 1000mercis@cp.assurance.returnpath.net
Delivered-To: assurance@localhost.returnpath.net
Received: from mxa-d1.returnpath.net (unknown [10.8.2.117])
    by cpa-d1.returnpath.net (Postfix) with ESMTP id 426E5198271
    for <1000mercis@cp.assurance.returnpath.net>; Fri,  1 Apr 2011 08:17:45 -0600 (MDT)
Received: from smtp-8-ft1.mm.fr.colt.net (smtp-7-ft1.mm.fr.colt.net [62.23.8.162])
    by mxa-d1.returnpath.net (Postfix) with ESMTP id 2906A1CD
    for <1000mercis@cp.assurance.returnpath.net>; Fri,  1 Apr 2011 08:17:44 -0600 (MDT)
Received: from host.25.62.23.62.rev.coltfrance.com ([62.23.62.25]:62162 helo=contact-darty.com)
    by massmail-ft1.infra.coltfrance.com with esmtp (Exim)
    id 1Q5fAU-00030S-4i
    for <1000mercis@cp.assurance.returnpath.net>; Fri, 01 Apr 2011 16:17:42 +0200
From: "Darty" <infos@contact-darty.com>
To: 1000mercis@cp.assurance.returnpath.net
Subject: Cuit Vapeur 29.90 euros, Nintendo 3DS 239 euros, GPS TOM TOM 139 euros... decouvrez VITE tous les bons plans du weekend !
Date: 01 Apr 2011 16:17:41 +0200
Message-ID: <20110401161739.E3786358A9D7B977@contact-darty.com>
MIME-Version: 1.0
x-idmail: DartyCRM_322_385774_10000
Content-Type: text/html;
    charset="iso-8859-1"
Content-Transfer-Encoding: 7bit
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title>Cuit Vapeur 29.90 euros, Nintendo 3DS 239 euros, GPS TOM TOM 139 euros... decouvrez VITE tous les bons plans du weekend !</title>
</head>
<body bottommargin="0" topmargin="0" rightmargin="0" leftmargin="0" marginheight="0" marginwidth="0" alink="#000000" vlink="#000000" link="#000000" bgcolor="#97bf0d">
<img src="http://contact-darty.com/_v.aspx?i=385774&ue=10000&m=322" width="1" height="1">
<img src="http://eulerian.darty.com/view/darty-fr/DEQwyRwgEDJm_8YpRfi44vHprIu2zZDqLE6L2ATS/pix.gif?eparam=DARTYCRM_M_322_385774_10000&eemail=1000mercis%40cp.assurance.returnpath.net" border="0" width="1" height="1" style="display:none;" nosend="">
<style type="text/css">
.ReadMsgBody {width: 100%;}
.ExternalClass {width: 100%;}
img {display:block}
</style>
<table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#97bf0d">
<tr><td align="center" valign="top" style="font-size:0px;">
<table border="0" cellspacing="0" cellpadding="0" width="653" bgcolor="#FFFFFF">
<tr><td align="center" valign="middle" style="font-family:Arial; font-size:10px; color:#000000;" width="653" height="25" bgcolor="#97bf0d">Si cet email ne s'affiche pas correctement, vous pouvez le visualiser <a href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=0" target="_blank" style="font-family:Arial; font-size:10px; color:#000000; text-decoration:none;"><font style="color:#000000;"><u>gr&acirc;ce &agrave; ce lien</u></font></a>.</td></tr>
<tr><td align="left" valign="top" style="font-size:0px;" width="653" height="38">
<table width="653" border="0" cellpadding="0" cellspacing="0"><tr>
<td align="left" valign="top" style="font-size:0px;" width="36" height="38"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=1"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_02.jpg" width="36" height="38" border="0" alt="Darty"></a></td>
<td align="left" valign="top" style="font-size:0px;" width="84" height="38"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=2"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_03.jpg" width="84" height="38" border="0" alt="Informatique"></a></td>
<td align="left" valign="top" style="font-size:0px;" width="55" height="38"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=3"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_04.jpg" width="55" height="38" border="0" alt="Console & Jeux"></a></td>
<td align="left" valign="top" style="font-size:0px;" width="90" height="38"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=4"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_05.jpg" width="90" height="38" border="0" alt="GPS, Autoradio & DVD portable"></a></td>
<td align="left" valign="top" style="font-size:0px;" width="79" height="38"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=5"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_06.jpg" width="79" height="38" border="0" alt="Photo & Cam&eacute;scopes"></a></td>
<td align="left" valign="top" style="font-size:0px;" width="51" height="38"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=6"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_07.jpg" width="51" height="38" border="0" alt="TV, HiFi & vid&eacute;o"></a></td>
<td align="left" valign="top" style="font-size:0px;" width="68" height="38"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=7"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_08.jpg" width="68" height="38" border="0" alt="Audio MP3 & MP4"></a></td>
<td align="left" valign="top" style="font-size:0px;" width="69" height="38"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=8"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_09.jpg" width="69" height="38" border="0" alt="T&eacute;l&eacute;phonie"></a></td>
<td align="left" valign="top" style="font-size:0px;" width="60" height="38"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=9"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_10.jpg" width="60" height="38" border="0" alt="Petit M&eacute;nager"></a></td>
<td align="left" valign="top" style="font-size:0px;" width="61" height="38"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=10"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_11.jpg" width="62" height="38" border="0" alt="Gros M&eacute;nager"></a></td>
</tr></table>
</td></tr>
<tr><td align="left" valign="top" style="font-size:0px;" width="653" height="145"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=11"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_13.jpg" width="654" height="160" border="0" alt="Darty"></a></td></tr>
<tr><td align="left" valign="top" style="font-size:0px;" width="653" height="14"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_14.jpg" width="653" height="14" border="0"></td></tr>
<!-- Debut 1er bloc -->
<tr><td align="left" valign="top" style="font-size:0px;" width="653" height="184">
<table width="653" border="0" cellpadding="0" cellspacing="0"><tr>
<td align="left" valign="top" style="font-size:0px;" width="21" height="190"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/spacer.gif" width="21" height="190" border="0"></td>
<td align="left" valign="top" style="font-size:0px;" width="306" height="184">
<table width="306" border="0" cellpadding="0" cellspacing="0">
<tr><td align="left" valign="top" style="font-size:0px;" width="306" height="57"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=12"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_16.jpg" width="306" height="57" border="0"></a></td></tr>
<tr><td align="left" valign="top" style="font-size:0px;" width="306" height="71">
<table width="306" border="0" cellpadding="0" cellspacing="0"><tr>
<td align="left" valign="top" style="font-size:0px;" width="17" height="77"><img src="http://mm.cache.coltfrance.com/Darty_CRM/img/mailing/00322/darty_19.jpg" width="17" height="77" border="0"></td>
<td align="left" valign="top" style="font-size:0px;" width="289" height="77">
<table width="289" border="0" cellpadding="0" cellspacing="0">
<tr><td align="left" valign="bottom" style="font-family:Arial; font-size:12px; color:#222222;" width="289" height="20"><a target="_blank" href="http://contact-darty.com/_c.aspx?i=385774&ue=10000&m=322&e=1000mercis%40cp.assurance.returnpath.net&r=13" style="font-family:Arial; font-size:12px; color:#222222; text-decoration:none;"><font style="color:#222222;"><b>Nintendo 3DS BLEU LAGON</b></font></a&...
"""
EMAIL_PARSE_API_V1_PATH = '/api/v1'

###
# Client
###

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

##
# Basic Unit Test
##

def test_health_check(client):
    rv = client.get(EMAIL_PARSE_API_V1_PATH + '/health')
    json_data = rv.get_json()
    assert json_data['status'] == "ok"

def test_api_email_parse_json(client):
    rv = client.post(EMAIL_PARSE_API_V1_PATH + '/email/parse', json={
        'emailRawText': RAW_EMAIL_MESSAGE
    })
    json_data = rv.get_json()
    print(json_data)
    assert json_data['date'] == '01 Apr 2011 16:17:41 +0200'
    assert json_data['subject'] == 'Cuit Vapeur 29.90 euros, Nintendo 3DS 239 euros, GPS TOM TOM 139 euros... decouvrez VITE tous les bons plans du weekend !'
    assert json_data['messageId'] == '<20110401161739.E3786358A9D7B977@contact-darty.com>'

def test_api_nothing_sent_return_400(client):
    rv = client.post(EMAIL_PARSE_API_V1_PATH + '/email/parse')
    assert rv.status_code == 400