# Installer Tools Berguna - via winget (sumber resmi Microsoft)
# Jalankan sebagai Administrator. Pilih kategori, script install satu per satu & melaporkan hasil.
$ErrorActionPreference = 'Continue'

$PaketInti = @(
  'Microsoft.PowerToys','voidtools.Everything','7zip.7zip','ShareX.ShareX',
  'Bitwarden.Bitwarden','Obsidian.Obsidian','VideoLAN.VLC','LocalSend.LocalSend'
)
$Kategori = @{
  '1' = @{ Nama='Paket Inti (Top 8)'; Paket=$PaketInti }
  '2' = @{ Nama='AI Lokal'; Paket=@('Ollama.Ollama','LMStudio.LMStudio') }
  '3' = @{ Nama='Developer'; Paket=@('Microsoft.VisualStudioCode','Git.Git','GitHub.cli','Microsoft.WindowsTerminal','Microsoft.PowerShell','OpenJS.NodeJS.LTS','Python.Python.3.13','Docker.DockerDesktop','Bruno.Bruno') }
  '4' = @{ Nama='Produktivitas'; Paket=@('Obsidian.Obsidian','Notion.Notion','TheDocumentFoundation.LibreOffice','Ditto.Ditto','SumatraPDF.SumatraPDF','Microsoft.PowerToys') }
  '5' = @{ Nama='Sistem'; Paket=@('voidtools.Everything','AntibodySoftware.WizTree','7zip.7zip','QL-Win.QuickLook') }
  '6' = @{ Nama='Multimedia'; Paket=@('OBSProject.OBSStudio','VideoLAN.VLC','HandBrake.HandBrake','Audacity.Audacity','KDE.Krita','BlenderFoundation.Blender','ShareX.ShareX') }
  '7' = @{ Nama='Keamanan'; Paket=@('Bitwarden.Bitwarden','KeePassXCTeam.KeePassXC','Malwarebytes.Malwarebytes','Cloudflare.Warp') }
  '8' = @{ Nama='Internet & Android'; Paket=@('Brave.Brave','Mozilla.Firefox','yt-dlp.yt-dlp','LocalSend.LocalSend','qBittorrent.qBittorrent','Genymobile.scrcpy','Google.PlatformTools') }
}

if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
  Write-Host 'winget TIDAK ditemukan. Install "App Installer" dari Microsoft Store dulu, lalu jalankan lagi.' -ForegroundColor Red
  exit 1
}
Write-Host "`n=== INSTALLER TOOLS BERGUNA ===" -ForegroundColor Cyan
$Kategori.GetEnumerator() | Sort-Object Name | ForEach-Object { Write-Host ("{0}) {1}" -f $_.Key, $_.Value.Nama) }
Write-Host "9) SEMUA KATEGORI"
$pilih = Read-Host 'Pilih nomor (pisahkan koma, contoh 1,3)'
$daftar = @()
if ($pilih -eq '9') { $daftar = $Kategori.Values.Paket | Select-Object -Unique }
else { foreach ($n in ($pilih -split ',')) { $k=$Kategori[$n.Trim()]; if ($k) { $daftar += $k.Paket } } }
$daftar = $daftar | Select-Object -Unique
if (-not $daftar) { Write-Host 'Pilihan kosong / tidak valid.'; exit }

Write-Host "`nAkan install $($daftar.Count) paket. Ini download dari sumber resmi, butuh internet." -ForegroundColor Yellow
if ((Read-Host 'Lanjut? ketik Y') -notmatch '^[Yy]') { exit }

$ok=@(); $gagal=@()
foreach ($id in $daftar) {
  Write-Host "`n>>> $id" -ForegroundColor Cyan
  winget install --id $id -e --accept-source-agreements --accept-package-agreements
  if ($LASTEXITCODE -eq 0) { $ok += $id } else { $gagal += $id }
}
Write-Host "`n========== HASIL ==========" -ForegroundColor Green
Write-Host "BERHASIL ($($ok.Count)): $($ok -join ', ')"
if ($gagal) { Write-Host "GAGAL / SUDAH ADA ($($gagal.Count)): $($gagal -join ', ')  <- coba install manual dari link resmi di repo" -ForegroundColor Yellow }
