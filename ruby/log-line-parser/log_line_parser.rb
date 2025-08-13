class LogLineParser
  def initialize(line)
    @message = line.partition(':').last.strip
    @log_level = line[/\[(.*?)\]/, 1].downcase
  end

  attr_reader :message, :log_level

  def reformat
    "#{message()} (#{log_level()})"
  end
end
