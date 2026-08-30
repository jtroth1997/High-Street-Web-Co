from pathlib import Path
import re

p = Path("tilers-community.html")
s = p.read_text()

s = s.replace(
    '<div class="mini-card"><strong>Project pictures come afterwards</strong><span>When this form is submitted we generate a unique project reference. Email your project photos to highstreetwebcompany@gmail.com using that reference in the subject line so everything can be matched to your build.</span></div>',
    '<div class="mini-card"><strong>Upload your project pictures with the brief</strong><span>Add your best finished-work photos before you submit. Your unique project reference will then stay with the job and will be used in the subject line when we send your first website draft and future project emails.</span></div>'
)

s = s.replace(
    '.photo-box{padding:18px;border-radius:16px;background:#f1ecff;border:1px solid #7557d326}.photo-box strong{display:block;margin-bottom:6px;font-size:13px}.photo-box p{margin:0;color:#5c5671;font-size:11px;line-height:1.55}',
    '.photo-box{padding:18px;border-radius:16px;background:#f1ecff;border:1px solid #7557d326}.photo-box strong{display:block;margin-bottom:6px;font-size:13px}.photo-box p{margin:0;color:#5c5671;font-size:11px;line-height:1.55}.photo-upload{display:block;margin-top:15px;padding:16px;border:1px dashed #a99bd8;border-radius:14px;background:#fff}.photo-upload input{padding:0;border:0;border-radius:0}.photo-status{display:block;margin-top:10px;font-size:10px;font-weight:650;line-height:1.5;color:#6c6384}.upload-capacity{display:flex;justify-content:space-between;gap:12px;margin-top:9px;font-size:10px;color:#6c6384}.upload-meter{height:7px;margin-top:8px;border-radius:999px;background:#ddd6f6;overflow:hidden}.upload-meter span{display:block;height:100%;width:0;background:#7557d3;transition:width .2s ease}'
)

s = s.replace(
    'Maximum 5MB. If you have several logo versions, upload your preferred one here.',
    'Maximum 2MB. This leaves as much of the 10MB attachment allowance as possible for your project photos.'
)

pattern = re.compile(r'<section class="form-section"><div class="section-title"><b>9</b><h3>Project pictures & final notes</h3></div>.*?</section>\n<div class="submit-row">', re.S)
replacement = '''<section class="form-section"><div class="section-title"><b>9</b><h3>Project pictures & final notes</h3></div><div class="photo-box"><strong>Upload your project photos here.</strong><p>Select your best completed-work images for the Gallery and throughout the site. You can attach up to <b>20 photos</b>. The logo and all photos together must stay within the <b>10MB total attachment limit</b>, so choose the strongest images rather than every photo from every job.</p><label class="photo-upload">Project photos<input id="project-photos" name="project_photos" type="file" accept="image/*" multiple required><span class="photo-status" id="photo-status">No photos selected yet. Aim for 6–12 strong images if possible.</span><div class="upload-capacity"><span id="photo-count">0 / 20 photos</span><span id="attachment-size">0.0 / 10MB used</span></div><div class="upload-meter" aria-hidden="true"><span id="upload-meter-fill"></span></div></label></div><label style="margin-top:18px">Gallery / project notes <small>(optional)</small><textarea name="gallery_notes" rows="4" placeholder="Tell us what the photos show, project locations, tile types, before/after sets or any captions we should know."></textarea></label><label>Anything else we need to know? <small>(optional)</small><textarea name="final_notes" rows="4" placeholder="Deadlines, launch dates, special requests or anything not covered above."></textarea></label><label class="check"><input type="checkbox" name="content_confirmation" required value="Confirmed">I confirm the information and images supplied can be used to build and publish my website, subject to my final approval.</label></section>
<div class="submit-row">'''
s, n = pattern.subn(replacement, s, count=1)
if n != 1:
    raise SystemExit("Could not replace section 9")

old_const = 'const codeInput=document.getElementById("referral-code"),unlockButton=document.getElementById("unlock"),gateMessage=document.getElementById("gate-message"),brief=document.getElementById("brief"),tcForm=document.getElementById("tc-form"),logo=document.getElementById("logo"),logoStatus=document.getElementById("logo-status"),logoFilename=document.getElementById("logo-filename"),projectReference=document.getElementById("project-reference"),refPreview=document.getElementById("ref-preview"),submitButton=document.getElementById("submit-button"),submitNote=document.getElementById("submit-note");'
new_const = 'const codeInput=document.getElementById("referral-code"),unlockButton=document.getElementById("unlock"),gateMessage=document.getElementById("gate-message"),brief=document.getElementById("brief"),tcForm=document.getElementById("tc-form"),logo=document.getElementById("logo"),logoStatus=document.getElementById("logo-status"),logoFilename=document.getElementById("logo-filename"),projectPhotos=document.getElementById("project-photos"),photoStatus=document.getElementById("photo-status"),photoCount=document.getElementById("photo-count"),attachmentSize=document.getElementById("attachment-size"),uploadMeterFill=document.getElementById("upload-meter-fill"),projectReference=document.getElementById("project-reference"),refPreview=document.getElementById("ref-preview"),submitButton=document.getElementById("submit-button"),submitNote=document.getElementById("submit-note");'
if old_const not in s:
    raise SystemExit("Could not find const declaration")
s = s.replace(old_const, new_const)

old_logo = 'logo.addEventListener("change",()=>{const file=logo.files?.[0];logoStatus.className="logo-status";if(!file){logoFilename.value="";return;}if(file.size>5*1024*1024){logo.value="";logoFilename.value="";logoStatus.textContent="That file is over 5MB. Please choose a smaller logo file.";logoStatus.classList.add("error");return;}logoFilename.value=file.name;logoStatus.textContent=`Selected: ${file.name} · ${(file.size/1024/1024).toFixed(2)}MB`;logoStatus.classList.add("success");});'
new_logo = '''function updateAttachmentStatus(){const logoFile=logo.files?.[0];const photos=Array.from(projectPhotos.files||[]);const total=(logoFile?.size||0)+photos.reduce((sum,f)=>sum+f.size,0);const mb=total/1024/1024;photoCount.textContent=`${photos.length} / 20 photos`;attachmentSize.textContent=`${mb.toFixed(1)} / 10MB used`;uploadMeterFill.style.width=`${Math.min(100,(mb/10)*100)}%`;photoStatus.className="photo-status";if(photos.length>20){photoStatus.textContent="Too many photos selected. Please choose no more than 20.";photoStatus.classList.add("error");return false;}if(total>10*1024*1024){photoStatus.textContent=`Your attachments total ${mb.toFixed(1)}MB. Please remove some photos until the total is 10MB or less.`;photoStatus.classList.add("error");return false;}if(photos.length){photoStatus.textContent=`${photos.length} project photo${photos.length===1?"":"s"} selected and ready to attach.`;photoStatus.classList.add("success");}else{photoStatus.textContent="No photos selected yet. Aim for 6–12 strong images if possible.";}return true;}
logo.addEventListener("change",()=>{const file=logo.files?.[0];logoStatus.className="logo-status";if(!file){logoFilename.value="";updateAttachmentStatus();return;}if(file.size>2*1024*1024){logo.value="";logoFilename.value="";logoStatus.textContent="That logo is over 2MB. Please choose a smaller logo file.";logoStatus.classList.add("error");updateAttachmentStatus();return;}logoFilename.value=file.name;logoStatus.textContent=`Selected: ${file.name} · ${(file.size/1024/1024).toFixed(2)}MB`;logoStatus.classList.add("success");updateAttachmentStatus();});
projectPhotos.addEventListener("change",()=>{if((projectPhotos.files?.length||0)>20){projectPhotos.value="";photoStatus.textContent="Please choose no more than 20 project photos.";photoStatus.className="photo-status error";}updateAttachmentStatus();});'''
if old_logo not in s:
    raise SystemExit("Could not find logo JS")
s = s.replace(old_logo, new_logo)

needle = 'if(!file){logoStatus.textContent="Please upload your logo before submitting.";logoStatus.classList.add("error");logo.scrollIntoView({behavior:"smooth",block:"center"});return;}const ref=makeReference();'
replacement_submit = 'if(!file){logoStatus.textContent="Please upload your logo before submitting.";logoStatus.classList.add("error");logo.scrollIntoView({behavior:"smooth",block:"center"});return;}if(!(projectPhotos.files?.length)){photoStatus.textContent="Please add at least one project photo before submitting.";photoStatus.className="photo-status error";projectPhotos.scrollIntoView({behavior:"smooth",block:"center"});return;}if(!updateAttachmentStatus()){projectPhotos.scrollIntoView({behavior:"smooth",block:"center"});return;}const ref=makeReference();'
if needle not in s:
    raise SystemExit("Could not find submit validation")
s = s.replace(needle, replacement_submit)
p.write_text(s)

t = Path("tilers-community-thank-you.html")
u = t.read_text()
u = u.replace(
    '<h1>Your project is now ready to match.</h1><p>Keep the reference below. Use it when you send your project photographs so we can connect the images with the business information and logo you have just submitted.</p>',
    '<h1>Your website brief is in.</h1><p>Keep the reference below for your records. It is now the permanent reference for this website project, and we will include it in the subject line when we email your first draft and future project updates.</p>'
)
old_steps = '<div class="steps"><div class="step"><b>1</b><div><strong>Email your project pictures</strong><p>Send your best finished-work photos to highstreetwebcompany@gmail.com. Original quality is best where possible.</p></div></div><div class="step"><b>2</b><div><strong>Put the reference in the subject</strong><p>Use the exact reference shown above so your images can be matched to your website brief immediately.</p></div></div><div class="step"><b>3</b><div><strong>Add any useful photo notes</strong><p>If you can, mention the job type, location, tile/material or which photos belong together.</p></div></div></div><div class="actions"><a class="button" id="email-photos" href="mailto:highstreetwebcompany@gmail.com">Email project pictures →</a><button class="button alt" id="copy" type="button">Copy reference</button></div><p class="small" id="copy-note">Do not send a second form. Your project reference is enough to match the photo email.</p>'
new_steps = '<div class="steps"><div class="step"><b>1</b><div><strong>Your information and photos are together</strong><p>Your website brief, logo and selected project images were submitted as one project.</p></div></div><div class="step"><b>2</b><div><strong>We build your first draft</strong><p>We will use the information you supplied as the starting point for the Home, About, Gallery and Contact pages.</p></div></div><div class="step"><b>3</b><div><strong>Watch for this reference</strong><p>When your first draft is ready, our email subject will include the exact project reference shown above so it is easy to keep everything together.</p></div></div></div><div class="actions"><button class="button" id="copy" type="button">Copy project reference</button><a class="button alt" href="index.html">Back to High Street Web Co.</a></div><p class="small" id="copy-note">You do not need to email your project photographs separately.</p>'
if old_steps not in u:
    raise SystemExit("Could not replace thank-you steps")
u = u.replace(old_steps, new_steps)

script_old_re = re.compile(r'const params=new URLSearchParams\(location\.search\);const ref=params\.get\("ref"\)\|\|sessionStorage\.getItem\("tcProjectReference"\)\|\|"TCWEB-REFERENCE";const refEl=document\.getElementById\("reference"\),email=document\.getElementById\("email-photos"\),copy=document\.getElementById\("copy"\),note=document\.getElementById\("copy-note"\);refEl\.textContent=ref;email\.href=`mailto:.*?`;copy\.addEventListener', re.S)
u, m = script_old_re.subn('const params=new URLSearchParams(location.search);const ref=params.get("ref")||sessionStorage.getItem("tcProjectReference")||"TCWEB-REFERENCE";const refEl=document.getElementById("reference"),copy=document.getElementById("copy"),note=document.getElementById("copy-note");refEl.textContent=ref;copy.addEventListener', u, count=1)
if m != 1:
    raise SystemExit("Could not update thank-you JS")
u = u.replace('note.textContent="Copied. Paste this reference into the subject of any additional emails for this website project.";', 'note.textContent="Copied. Keep this reference with your records; we will use it on the first-draft email.";')
t.write_text(u)
