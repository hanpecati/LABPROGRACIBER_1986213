function Search-Tags
{	
	$etiqueta1 = Read-Host "Etiqueta de busqueda"
	$etiqueta2 = Read-Host "Etiqueta de busqueda"
	$etiqueta3 = Read-Host "Etiqueta de busqueda"
	START http://www.news.google.com/search?q=$etiqueta1%20when%3A1d
	START http://www.news.google.com/search?q=$etiqueta2%20when%3A1d
	START http://www.news.google.com/search?q=$etiqueta3%20when%3A1d
}
function Search-News
{
	Search-Tags
}
$validate = Read-Host "Iniciar busqueda: Si[Y] No [N]?"

if ($validate -eq "Y")
{
	Search-News
	Write-Host "Searching..."
	Write-Host "Busqueda iniciada con las etiquetas:" $etiqueta1, $etiqueta2, $etiqueta3
}
ElseIf ($validate -eq "N")
{
	Write-Host "Canceling search..."
}