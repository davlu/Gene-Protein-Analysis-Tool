
import click

from analytics import DNAanalysis 

@click.group(invoke_without_command=True)
@click.option('--dna-string', '-d', default=None,
	help=('DNA string to run ATGC content analysis on'))
def main(dna_string):
	if not dna_string is None:
		content = DNAanalysis.ATGC_content(dna_string)
		message = click.style('DNA string contains the following nucleotides:\n', 
			fg='magenta', bold=True)
		for k, v in content.items():
			base = click.style(k, fg='yellow', bold=True)
			content_count = click.style(str(v), fg='magenta', bold=True)
			count_width = 4
			message += f'{base}: {content_count:{count_width}}\n'
		click.echo(message)
