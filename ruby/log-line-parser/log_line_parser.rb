class LogLineParser
  def initialize(line)
    @line = line
  end

  def message
    message_start_index = @line.index(":") + 1
    @line[message_start_index..].strip
  end

  def log_level
    start_index = @line.index("[") + 1
    end_index = @line.index("]") - 1
    @line[start_index..end_index].downcase
  end

  def reformat
    "#{message()} (#{log_level()})"
  end
end
