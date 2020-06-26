
# coding: utf-8

# In[1]:


import pandas


# In[2]:


from urllib.request import urlopen


# In[3]:


from bs4 import BeautifulSoup


# In[4]:


html = urlopen("https://parivahan.gov.in/rcdlstatus/?pur_cd=101")


# In[5]:


print(html.read())


# In[6]:


bsobj = BeautifulSoup(html.read(),'lxml')


# In[7]:


print(bsobj.body)


# In[8]:


print(bsobj.div)


# In[9]:


print(bsobj.prettify)


# In[10]:


print(bsobj.html)


# In[11]:


html_doc = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"><head id="j_idt2"><link type="text/css" rel="stylesheet" href="/rcdlstatus/vahan/javax.faces.resource/theme.css?ln=primefaces-parivahan" /><link type="text/css" rel="stylesheet" href="/rcdlstatus/vahan/javax.faces.resource/grid-css.css?ln=css" /><link type="text/css" rel="stylesheet" href="/rcdlstatus/vahan/javax.faces.resource/layout.css?ln=css" /><link type="text/css" rel="stylesheet" href="/rcdlstatus/vahan/javax.faces.resource/css/bootstrap.min.css?ln=bootstrap-3.3.7" /><link type="text/css" rel="stylesheet" href="/rcdlstatus/vahan/javax.faces.resource/components.css?ln=primefaces&amp;v=6.0" /><script type="text/javascript" src="/rcdlstatus/vahan/javax.faces.resource/jquery/jquery.js?ln=primefaces&amp;v=6.0"></script><script type="text/javascript" src="/rcdlstatus/vahan/javax.faces.resource/jquery/jquery-plugins.js?ln=primefaces&amp;v=6.0"></script><script type="text/javascript" src="/rcdlstatus/vahan/javax.faces.resource/core.js?ln=primefaces&amp;v=6.0"></script><script type="text/javascript" src="/rcdlstatus/vahan/javax.faces.resource/components.js?ln=primefaces&amp;v=6.0"></script><script type="text/javascript" src="/rcdlstatus/vahan/javax.faces.resource/keyfilter/keyfilter.js?ln=primefaces&amp;v=6.0"></script><script type="text/javascript" src="/rcdlstatus/vahan/javax.faces.resource/jsf.js?ln=javax.faces"></script><script type="text/javascript">if(window.PrimeFaces){PrimeFaces.settings.locale='en_US';}</script>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
        <meta http-equiv="refresh" content="600;url=https://parivahan.gov.in/parivahan/" />
        <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Open+Sans" />
        <title>RC/DL STATUS</title>
        <link rel="shortcut icon" type="image/x-icon" href="/rcdlstatus/vahan/javax.faces.resource/images/vahan_icon.ico" />
        <link type="text/css" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css" media="all" /><script type="text/javascript" src="/rcdlstatus/vahan/javax.faces.resource/js/bootstrap.min.js?ln=bootstrap-3.3.7"></script><script type="text/javascript" src="/rcdlstatus/vahan/javax.faces.resource/utils.js?ln=js"></script>        
        <script>
            $(document).on("input", ".numeric", function() {
                this.value = this.value.replace(/[^\d\.\-]/g, '');
            });
        </script>
        <script>
            function changemysize(myvalue) {
                var div = document.getElementById("mymain");
                div.style.fontSize = myvalue + "px";
            }
        </script>
        <link type="text/css" rel="stylesheet" href="//cdn.jsdelivr.net/bootstrap/3.3.5/css/bootstrap.css" media="all" /></head><body id="mymain">
<form id="form_rcdl" name="form_rcdl" method="post" action="/rcdlstatus/vahan/rcDlHome.xhtml" enctype="application/x-www-form-urlencoded">
<input type="hidden" name="form_rcdl" value="form_rcdl" />

            <div class="ui-grid ui-grid-responsive">
                <div class="skip-navigation-section">
                    <div class="container">
                        <div class="right-position text-resize-section">
                            <ul>
                                <li class="skip-section"> 
                                    <a href="https://parivahan.gov.in/parivahan" title="Home">
                                        <i class="fa fa-home fa-text-color"></i> Home</a>
                                </li>
                                <li class="skip-section"> 
                                    <a href="#main-content">
                                        <i class="fa fa-arrow-down"></i> Skip to main content</a>
                                </li>
                                <li class="skip-section"> 
                                    <a href="#navbar">
                                        <i class="fa fa-arrow-down"></i> Skip to navigation</a>
                                </li>
                                <li>
                                    <a href="javascript:void(0);" onclick="changemysize(10);" style="text-decoration: none;" id="decfont">A<sup>-</sup></a>
                                </li>
                                <li>
                                    <a href="javascript:void(0);" onclick="changemysize(12);" style="text-decoration: none;" id="resetfont"> A</a>
                                </li>
                                <li>
                                    <a href="javascript:void(0);" onclick="changemysize(16);" style="text-decoration: none;" id="incfont">A<sup>+</sup></a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="logo-header-section">
                    <div class="container">
                        <div class="inline-section vertical-right-divider">
                            <div id="logo">
                                <a href="https://parivahan.gov.in/parivahan" title="Home">
                                    <img src="HTTPS://parivahan.gov.in/parivahan/sites/default/files/logo-parivahan-sewa-en.png" class="emblem-resize" /></a>
                            </div>
                        </div>
                        <div class="inline-section fix-width">
                            <div class="govt-india">
                                Government of India 
                            </div>
                            <div class="slogan-name">
                                Ministry of Road Transport &amp; Highways       
                            </div>
                        </div>
                    </div>
                </div>
                <nav class="navbar navbar-default navigation-background-nav" role="navigation">
                    <div class="container">
                        <div class="navbar-header">
                            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                                <span class="sr-only">Toggle navigation</span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </button>
                        </div>
                        <div class="collapse navbar-collapse" id="navbar">
                            <ul class="nav navbar-nav">
                                <li data-id="347" data-level="1" data-type="menu_item" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega">
                                    <a href="https://parivahan.gov.in/parivahan">Home</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>

                <div class="container">
                    <div class="top-space bottom-space"><div id="form_rcdl:rcdl_pnl" class="ui-panel ui-widget ui-widget-content ui-corner-all datatable-panel" data-widget="widget_form_rcdl_rcdl_pnl"><div id="form_rcdl:rcdl_pnl_header" class="ui-panel-titlebar ui-widget-header ui-helper-clearfix ui-corner-all"><span class="ui-panel-title">Know your DL Status</span></div><div id="form_rcdl:rcdl_pnl_content" class="ui-panel-content ui-widget-content"><div id="form_rcdl:j_idt13" class="ui-messages ui-widget" aria-live="polite"></div><div id="form_rcdl:j_idt15" class="ui-outputpanel ui-widget">
                                <div class="ui-grid-row bottom-space">
                                    <div class="ui-grid-col-4 resp-blank-height"></div>
                                    <div class="ui-grid-col-2">
                                        <label class="field-label resp-label-section"><label id="form_rcdl:j_idt17" class="ui-outputlabel ui-widget top-space field-label-mandate" for="form_rcdl:tf_dlNO">Driving Licence No.<span class="ui-outputlabel-rfi">*</span></label>
                                        </label>
                                    </div>
                                    <div class="ui-grid-col-3"><script id="form_rcdl:j_idt19_s" type="text/javascript">$(function(){PrimeFaces.cw("KeyFilter","widget_form_rcdl_j_idt19",{id:"form_rcdl:j_idt19",target:"form_rcdl:tf_dlNO",regEx:/[A-Z0-9- /.]/i,preventPaste:true});});</script><input id="form_rcdl:tf_dlNO" name="form_rcdl:tf_dlNO" type="text" autocomplete="off" maxlength="20" placeholder="DL-12345678901234" size="16" onchange="PrimeFaces.ab({s:&quot;form_rcdl:tf_dlNO&quot;,e:&quot;valueChange&quot;,p:&quot;form_rcdl:tf_dlNO&quot;,u:&quot;form_rcdl:tf_dlNO&quot;});" aria-required="true" class="ui-inputfield ui-inputtext ui-widget ui-state-default ui-corner-all input" /><script id="form_rcdl:tf_dlNO_s" type="text/javascript">PrimeFaces.cw("InputText","widget_form_rcdl_tf_dlNO",{id:"form_rcdl:tf_dlNO"});</script>
                                    </div>
                                </div>
                                <div class="ui-grid-row bottom-space">
                                    <div class="ui-grid-col-4 resp-blank-height"></div>
                                    <div class="ui-grid-col-2">
                                        <label class="field-label resp-label-section right-position"><label id="form_rcdl:j_idt22" class="ui-outputlabel ui-widget top-space field-label-mandate" for="form_rcdl:tf_dob_input">Date Of Birth<span class="ui-outputlabel-rfi">*</span></label>
                                        </label>
                                    </div>
                                    <div class="ui-grid-col-3"><span id="form_rcdl:tf_dob" class="ui-calendar input"><input id="form_rcdl:tf_dob_input" name="form_rcdl:tf_dob_input" type="text" aria-required="true" class="ui-inputfield ui-widget ui-state-default ui-corner-all" autocomplete="off" maxlength="12" placeholder="31-01-1990" onchange="PrimeFaces.ab({s:&quot;form_rcdl:tf_dob&quot;,e:&quot;valueChange&quot;,p:&quot;form_rcdl:tf_dob&quot;,u:&quot;form_rcdl:tf_dob&quot;,ps:true});" aria-labelledby="form_rcdl:j_idt22" /></span><script id="form_rcdl:tf_dob_s" type="text/javascript">$(function(){PrimeFaces.cw("Calendar","widget_form_rcdl_tf_dob",{id:"form_rcdl:tf_dob",popup:true,locale:"en_US",dateFormat:"dd-mm-yy",maxDate:"26-06-2020",yearRange:"1900:c",changeMonth:true,changeYear:true,behaviors:{}});});</script>
                                    </div>
                                </div></div><div id="form_rcdl:captchaPnl" class="ui-outputpanel ui-widget">
                                <div class="ui-grid-row bottom-space">                        
                                    <div class="ui-grid-col-4 resp-blank-height"></div>
                                    <div class="ui-grid-col-8 inline-section field-label-mandate">
                <div class="ui-grid-row"> 
                    <div class="ui-grid-col-3">
                        <label class="field-label resp-label-section"><label id="form_rcdl:j_idt32:j_idt35" class="ui-outputlabel ui-widget" for="form_rcdl:j_idt32:CaptchaID">Enter Verification Code<span class="ui-outputlabel-rfi">*</span></label> 
                        </label>
                    </div>
                    <div class="ui-grid-col-6"><table class="vahan-captcha inline-section">
<tbody>
<tr>
<td><img id="form_rcdl:j_idt32:j_idt38" src="/rcdlstatus/DispplayCaptcha?txtp_cd=1&amp;bkgp_cd=2&amp;noise_cd=2&amp;gimp_cd=3&amp;txtp_length=5&amp;pfdrid_c=true?-1755034948&amp;pfdrid_c=true" alt="" /></td>
<td><img id="form_rcdl:j_idt32:j_idt39" width="5" alt="" src="/rcdlstatus/vahan/javax.faces.resource/spacer/dot_clear.gif?ln=primefaces&amp;v=6.0" /></td>
<td><input id="form_rcdl:j_idt32:CaptchaID" name="form_rcdl:j_idt32:CaptchaID" type="text" value="" autocomplete="off" maxlength="5" size="10" onblur="mojarra.ab('form_rcdl:j_idt32:CaptchaID',event,'blur','@this','@this',{'CLIENT_BEHAVIOR_RENDERING_MODE':'OBSTRUSIVE'})" style="width: 67% !important;" aria-required="true" class="ui-inputfield ui-inputtext ui-widget ui-state-default ui-corner-all" /><script id="form_rcdl:j_idt32:CaptchaID_s" type="text/javascript">PrimeFaces.cw("InputText","widget_form_rcdl_j_idt32_CaptchaID",{id:"form_rcdl:j_idt32:CaptchaID"});</script></td>
</tr>
</tbody>
</table>

                    </div>
                </div>
                                    </div>                        
                                </div></div>
                            
                            <div class="ui-grid-row bottom-space center-position">
                                <div class="ui-grid-col-12"><button id="form_rcdl:j_idt43" name="form_rcdl:j_idt43" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" onclick="PrimeFaces.ab({s:&quot;form_rcdl:j_idt43&quot;,u:&quot;form_rcdl:pnl_show form_rcdl:pg_show form_rcdl:rcdl_pnl&quot;,onst:function(cfg){PF('block_ui').show();;},onsu:function(data,status,xhr){PF('block_ui').hide();;}});return false;" type="submit"><span class="ui-button-text ui-c">Check Status</span></button><script id="form_rcdl:j_idt43_s" type="text/javascript">PrimeFaces.cw("CommandButton","widget_form_rcdl_j_idt43",{id:"form_rcdl:j_idt43"});</script><button id="form_rcdl:rest_bt" name="form_rcdl:rest_bt" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" onclick="" type="submit"><span class="ui-button-text ui-c">Reset</span></button><script id="form_rcdl:rest_bt_s" type="text/javascript">PrimeFaces.cw("CommandButton","widget_form_rcdl_rest_bt",{id:"form_rcdl:rest_bt"});</script>                    
                                </div>
                            </div><div id="form_rcdl:pnl_show" class="ui-outputpanel ui-widget datatable-panel"></div><div id="form_rcdl:j_idt45" class="ui-outputpanel ui-widget">
                                <div class="ui-grid-row">
                                    <div class="ui-grid-col-1 right-position right-space" style="width: 5% !important">
                                        <b style="font-size: 14px !important"><u>Note:</u> - </b>
                                    </div>
                                    <div class="ui-grid-col-11">
                                        <span class="text-red" style="font-size: 13px !important">Driving Licence number can be entered in any of the following formats: DL-1420110012345 or DL14 20110012345<br />
                                            Total number of input characters should be exactly 16 (including space or '-').<br />
                                            If you hold an old driving license with a different format, please convert the format as per below rule before entering.<br />
                                            <b>SS-RRYYYYNNNNNNN</b> OR  <b>SSRR YYYYNNNNNNN</b><br />
                                            Where<br />
                                            <b>SS</b> - Two character State Code (like RJ for Rajasthan, TN for Tamil Nadu etc)<br />
                                            <b>RR</b> - Two digit RTO Code<br />
                                            <b>YYYY</b> - 4-digit Year of Issue (For Example: If year is mentioned in 2 digits, say 99, then it should be converted to 1999. Similarly use 2012 for 12).<br />
                                            Rest of the numbers are to be given in 7 digits. If there are less number of digits, then additional 0's(zeros) may be added to make the total 7.<br />
                                            For example: If the Driving Licence Number is  RJ-13/DLC/12/ 123456 then please enter RJ-1320120123456 OR RJ13 20120123456.</span>
                                    </div>
                                </div></div></div></div><script id="form_rcdl:rcdl_pnl_s" type="text/javascript">PrimeFaces.cw("Panel","widget_form_rcdl_rcdl_pnl",{id:"form_rcdl:rcdl_pnl"});</script>
                    </div><div id="form_rcdl:j_idt48" class="ui-blockui-content ui-widget ui-widget-content ui-corner-all ui-helper-hidden ui-shadow"><img id="form_rcdl:j_idt49" src="/rcdlstatus/vahan/javax.faces.resource/ajax_loader_blue.gif?ln=images" alt="" width="30%" height="40%" /></div><script id="form_rcdl:j_idt48_s" type="text/javascript">$(function(){PrimeFaces.cw("BlockUI","block_ui",{id:"form_rcdl:j_idt48",block:"form_rcdl"});});</script>

                    <div class="center-position"> 
                        <h1 class="header-main text-underline">Terms Of Uses</h1>
                        <div>
                            <ul class="borderstyle">
                                <li>The content on this portal is meant for sharing information regarding vehicles on the basis of information available on centralized VAHAN and vehicle National Register. Using content of this portal for any commercial purpose or any derivative work or misuse of any kind is strictly prohibited and may invite legal consequences. </li>
                                <li>The content can be removed from the portal without notice and at any time as per Ministry of Road Transport and Highways/NIC direction.</li>
                                <li>Ministry of Road Transport and Highways/NIC shall not be held responsible for any interactions/passing of information(s) etc. between any user via e-mail, chat and any other mediation with another user. Ministry of Road Transport and Highways/NIC has no obligation to monitor any such disputes arising between the users and shall not be party to such dispute/litigation etc.</li>
                                <li>These terms and conditions shall be governed by and construed in accordance with the Indian Laws. Any dispute arising under these terms and conditions shall be subject to the jurisdiction of the courts of Indian territory only.</li>
                            </ul> 
                        </div>
                    </div>
                </div>
                <div class="ui-grid-row top-space">
                    <div class="ui-grid-col-12"><html xmlns="http://www.w3.org/1999/xhtml"><head id="form_rcdl:j_idt52"><link type="text/css" rel="stylesheet" href="/rcdlstatus/vahan/javax.faces.resource/theme.css?ln=primefaces-parivahan" /><script type="text/javascript">if(window.PrimeFaces){PrimeFaces.settings.locale='en_US';}</script>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="shortcut icon" href="/rcdlstatus/images/vahan_icon.ico" /></head><body>
        <div class="vahan-footer-section">
            <div class="ui-grid-row">
                <div class="ui-grid-col-3 left-position">

                    <div class="inline-section footer-line-height right-space">
                        <a href="http://www.nic.in/" target="_blank"><img id="form_rcdl:j_idt58" src="/rcdlstatus/vahan/javax.faces.resource/nic-logo.png?ln=images" alt="" /></a>
                    </div>
                </div>
                <div class="ui-grid-col-6 center-position">
                    <div class="inline-section top-space">
                        This Website belongs to Ministry of Road Transport &amp; Highways (MoRTH)
                        <br />
                        Government of India
                    </div>
                </div>
                <div class="ui-grid-col-3 right-position footer-line-height">

                    <div class="inline-section footer-line-height">
                        <a href="http://www.digitalindia.gov.in/" target="_blank"><img id="form_rcdl:j_idt62" src="/rcdlstatus/vahan/javax.faces.resource/digital-india.jpg?ln=images" alt="" style="width: 75px;" /></a>
                    </div>
                </div>
            </div>
        </div></body>
</html>
                    </div>
                </div>
            </div><input type="hidden" name="javax.faces.ViewState" id="j_id1:javax.faces.ViewState:0" value="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" autocomplete="off" />
</form></body>
</html>"""


# In[13]:


soup = BeautifulSoup(html_doc,'html.parser')


# In[14]:


print(soup.body)


# In[15]:


print(soup.head)


# In[16]:


print(soup.head.title)


# In[17]:


el = soup.find('div')


# In[18]:


print(el)


# In[21]:


for item in soup.select('.item'):
    print(item.get_text())


# In[23]:


import requests
from bs4 import BeautifulSoup
from csv import writer


# In[27]:


response= requests.get('https://parivahan.gov.in/rcdlstatus/?pur_cd=101')

response
# In[28]:


print(response)


# In[29]:


soup = BeautifulSoup(response.text,'html.parser')

re=soup.findAll()