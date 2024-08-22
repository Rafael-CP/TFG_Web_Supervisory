PROGRAM _INIT
<?xml version="1.0"?>
<?AutomationStudio FileVersion="4.9"?>
<!-- Automation Studio Generated XML Section -->
<networks maxcolumn="0">
	<network label="" comment="" row="1" column="0" commented="0">
		<row>
			<analog type="input" name="FALSE"/>
			<function position="topbottom" type="MOVE"><input name="" extensible="true"/><output name="40"/></function>
			<analog type="output" name="Alarm1.Status"/>
		</row>
	</network>
	<network label="" comment="" row="1" column="0" commented="0">
		<row>
			<analog type="input" name="&quot;Motor em estado de erro!&quot;"/>
			<function position="topbottom" type="MOVE"><input name="" extensible="true"/><output name="40"/></function>
			<analog type="output" name="Alarm1.Description"/>
		</row>
	</network>
	<network label="" comment="" row="1" column="0" commented="0">
		<row>
			<analog type="input" name="1"/>
			<function position="topbottom" type="MOVE"><input name="" extensible="true"/><output name="40"/></function>
			<analog type="output" name="Alarm1.Severity"/>
		</row>
	</network>
	<network label="" comment="" row="1" column="0" commented="0">
		<row>
			<analog type="input" name="0"/>
			<function position="topbottom" type="MOVE"><input name="" extensible="true"/><output name="40"/></function>
			<analog type="output" name="Alarm1.Acknowledgement"/>
		</row>
	</network>
</networks>
END_PROGRAM


